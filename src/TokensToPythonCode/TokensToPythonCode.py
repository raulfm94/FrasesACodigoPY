from enum import Enum


class Modify(Enum):
    INCREMENT = 1
    DECREMENT = -1


nouns = ["NN", "NNP"]


def stringify(unquoted_string):
    return '"' + unquoted_string + '"'

# for all format classes, string values must be passed with quotes included
# (i.e., single quote-wrapped)
# ex: instead of "happy" -> '"happy"'


def format_tab_string(num_tabs):
    return_string = ""
    for i in range(num_tabs):
        return_string += "\t"
    return return_string


def format_class_initialization(name):
    return "class " + name + ":\n"


def format_attribute_assignment(attribute_name, attribute_value,
                                num_tabs, is_self):
    return_string = format_tab_string(num_tabs)
    if is_self:
        return_string += "self."
    return return_string + attribute_name + " = " + str(attribute_value) + "\n"


def format_attribute_modification(attribute_name, modification_type,
                                  modifier_value, num_tabs, is_self):
    return_string = format_tab_string(num_tabs)
    if is_self:
        return_string += "self."
    if modification_type == Modify.INCREMENT:
        return return_string + attribute_name + " += " + str(modifier_value) + "\n"
    elif modification_type == Modify.DECREMENT:
        return return_string + attribute_name + " -= " + str(modifier_value) + "\n"


def format_return_statement(return_value, num_tabs):
    tabs_string = format_tab_string(num_tabs)
    return tabs_string + "return " + str(return_value) + "\n"


# pass print_values as a list, maintaining string quotes, if needed
def format_print_statement(print_value, num_tabs):
    tab_string = format_tab_string(num_tabs)
    if not print_value:
        return tab_string + "print\n"
    else:
        return_string = tab_string + "print " + str(print_value) + "\n"
        return return_string


# pass method_parameters as a list, maintaining string quotes, if needed
def format_invoke_method(method_name, method_parameters, num_tabs, is_self):
    return_string = format_tab_string(num_tabs)
    if is_self:
        return_string += "self."
    if not method_parameters:
        return return_string + method_name + "()\n"
    else:
        return_string = return_string + method_name + "(" + str(method_parameters[0])
        for parameter in method_parameters[1:]:
            return_string += ", " + str(parameter)
        return_string += ")\n"
        return return_string


# pass method_parameters as a list
def format_method_declaration(method_name, method_parameters):
    if not method_parameters:
        return "\n\tdef " + method_name + "(self):\n"
    else:
        return_string = "\n\tdef " + method_name + "(self, " + str(method_parameters[0])
        for parameter in method_parameters[1:]:
            return_string += ", " + str(parameter)
        return_string += "):\n"
        return return_string


def build_code_string(tokens):
    current_token = 0
    code_string = ""

    while tokens[current_token][0] not in nouns:
        current_token += 1
    code_string += format_class_initialization(tokens[current_token][1])

    while tokens[current_token][0] != "PRP":
        current_token += 1
    current_token += 1

    while tokens[current_token][0] != "TO":
        if tokens[current_token][0] == "ASSIGN":
            if tokens[current_token + 1][0] == "CD":
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           tokens[current_token + 1][1], 1, False)
            elif tokens[current_token + 1][0] == "STRSTART":
                temp_string = ""
                temp_token_count = 2
                while tokens[current_token + temp_token_count][0] != "STRSTOP" and \
                        tokens[current_token + temp_token_count][0] != "STRSTART":
                    temp_string += tokens[current_token + temp_token_count][1]
                    temp_token_count += 1
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           stringify(temp_string), 1, False)
            elif tokens[current_token + 1][0] == "TRUE":
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           True, 1, False)
            elif tokens[current_token + 1][0] == "FALSE":
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           False, 1, False)
            elif tokens[current_token + 1][0] == "PARL":
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           "(" + tokens[current_token + 2][1] + ")", 1, False)
            elif tokens[current_token + 1][0] == "BRACKL":
                code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                           "[" + tokens[current_token + 2][1] + "]", 1, False)
        current_token += 1

    while current_token < len(tokens) - 1:
        if tokens[current_token][0] == "TO":
            current_token += 1
            if tokens[current_token + 2][0] == "PARAMVERB":
                params = []
                temp_token_count = 3
                while tokens[current_token + temp_token_count][0] in nouns or \
                        tokens[current_token + temp_token_count][0] == ",":
                    if tokens[current_token + temp_token_count][0] in nouns:
                        params.append(tokens[current_token + temp_token_count][1])
                        temp_token_count += 1
                    else:
                        temp_token_count += 1
                code_string += format_method_declaration(tokens[current_token][1], params)
                current_token += temp_token_count
            else:
                code_string += format_method_declaration(tokens[current_token][1], None)
                current_token += 2

            while tokens[current_token][0] != "TO" and current_token < len(tokens) - 1:
                if tokens[current_token][0] == "BODYVERB":
                    params = []
                    temp_token_count = 3
                    while tokens[current_token + temp_token_count][0] != "PARR":
                        if tokens[current_token + temp_token_count][0] != ",":
                            params.append(tokens[current_token + temp_token_count][1])
                            temp_token_count += 1
                        if tokens[current_token + temp_token_count][0] == ",":
                            temp_token_count += 1
                    code_string += format_invoke_method(tokens[current_token + 1][1], params, 2, True)
                    current_token += temp_token_count + 1
                if tokens[current_token][0] == "ASSIGN":
                    if tokens[current_token + 1][0] == "CD":
                        code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                                   tokens[current_token + 1][1], 2, True)
                        current_token += 1
                    elif tokens[current_token + 1][0] == "STRSTART":
                        temp_string = ""
                        temp_token_count = 2
                        while tokens[current_token + temp_token_count][0] != "STRSTOP" and \
                                tokens[current_token + temp_token_count][0] != "STRSTART":
                            temp_string += tokens[current_token + temp_token_count][1]
                            temp_token_count += 1
                        code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                                   stringify(temp_string), 2, True)
                        current_token += temp_token_count
                    elif tokens[current_token + 1][0] == "TRUE":
                        code_string += format_attribute_assignment(tokens[current_token - 1][1], True, 2, True)
                        current_token += 1
                    elif tokens[current_token + 1][0] == "FALSE":
                        code_string += format_attribute_assignment(tokens[current_token - 1][1], False, 2, True)
                        current_token += 1
                    elif tokens[current_token + 1][0] == "PARL" or "BRACKL":
                        code_string += format_attribute_assignment(tokens[current_token - 1][1],
                                                                   tokens[current_token + 2][1], 2, True)
                        current_token += 3
                elif tokens[current_token][0] == "SUBS":
                    if tokens[current_token - 1][0] == "BRACKR":
                        index_access = tokens[current_token - 4][1] + "[" + tokens[current_token - 2][1] + "]"
                        code_string += format_attribute_modification(index_access, Modify.DECREMENT,
                                                                     tokens[current_token + 1][1], 2, True)
                        current_token += 1
                    else:
                        code_string += format_attribute_modification(tokens[current_token - 1][1], Modify.DECREMENT,
                                                                     tokens[current_token + 1][1], 2, True)
                        current_token += 1
                elif tokens[current_token][0] == "ADD":
                    if tokens[current_token - 1][0] == "BRACKR":
                        index_access = tokens[current_token - 4][1] + "[" + tokens[current_token - 2][1] + "]"
                        code_string += format_attribute_modification(index_access, Modify.INCREMENT,
                                                                     tokens[current_token + 1][1], 2, True)
                        current_token += 1
                    else:
                        code_string += format_attribute_modification(tokens[current_token - 1][1], Modify.INCREMENT,
                                                                     tokens[current_token + 1][1], 2, True)
                        current_token += 1
                elif tokens[current_token][0] == "RETURN":
                    code_string += format_return_statement(tokens[current_token + 1][1], 2)
                    current_token += 2
                elif tokens[current_token][0] == "PRINT":
                    temp_string = ""
                    temp_token_count = 1

                    while tokens[current_token + temp_token_count][0] != "PTRSTOP" and \
                            tokens[current_token + temp_token_count][0] != ",":
                        if tokens[current_token + temp_token_count][0] == "STRSTART":
                            temp_string += '"'
                            temp_token_count += 1
                            while tokens[current_token + temp_token_count][0] != "STRSTOP" and \
                                    tokens[current_token + temp_token_count][0] != "STRSTART":
                                temp_string += tokens[current_token + temp_token_count][1]
                                temp_token_count += 1
                            if tokens[current_token + temp_token_count][0] == "STRSTART":
                                temp_token_count += 1
                            temp_string += '"'
                        else:
                            temp_string += tokens[current_token + temp_token_count][1]
                            temp_token_count += 1
                    code_string += format_print_statement(temp_string, 2)
                    current_token += temp_token_count
                else:
                    current_token += 1
    return code_string


def tokenize(file_name):
    file = open(file_name, "r")
    word = ""
    list1 = []
    list2 = []
    i = 0
    read = False
    with file as fileobj:
        for line in fileobj:
            for ch in line:
                if ch == "\'" and not read:
                    read = True
                    i += 1
                    continue
                if read and ch == "\'":
                    read = False
                    if i % 2 == 0:
                        list1.append(word)
                    elif i % 2 != 0:
                        list2.append(word)
                    word = ""
                if read:
                    word += ch
    zipped = zip(list1, list2)
    file.close()
    return list(zipped)


def print_to_file(content):
    with open("../../output/compiled_python.py", "w") as txt_file:
        txt_file.write(content)


# tokenizer debugging
def print_tuple(tokens):
    for item in tokens:
        print item
    print "\n"


def convert_to_code():
    if __name__ == "__main__":
        file_name = "../tokens.txt"
        tokens = tokenize(file_name)
        # print_tuple(tokens)
        # print build_code_string(tokens)
        print_to_file(build_code_string(tokens))