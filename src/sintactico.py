
def tokens_from_file(name_of_file):
    file = open(name_of_file, "r")
    word = ""
    list1 = []
    list2 = []
    i = 0
    read = False
    with file as fileobj:
        for line in fileobj:
            for ch in line:
                if ch == "\'" and read == False:
                    read = True
                    i+=1
                    continue
                if read == True and ch == "\'":
                    read = False
                    if i % 2 == 0:
                        list1.append(word)
                    elif i % 2 != 0:
                        list2.append(word)
                    word = ""
                if(read == True):
                    word += ch
        list1.append('')
        list2.append('')
    zipped = zip(list2,list1,)
    file.close()
    return list(zipped)

# def access_to_touple(tokens):
#     for item in tokens:
#         print ("A tuple", item)
#     for a, b in tokens:
#         print ("First", a, "then", b)
#     print(tokens[1])

iterator = 0

def empatar():
    global iterator
    iterator=iterator + 1

# Class -> Class_Definition Attribute_Definition Functions
def classs(tokens):
    res = False
    if class_definition(tokens) and attribute_definition(tokens) and functions(tokens):
        res = True
    return res

# Class_Definition -> Noun "ASSIGN" "CLASS"
def class_definition(tokens):
    if noun(tokens):
        if tokens[iterator][1] == "ASSIGN":
            empatar()
            if tokens[iterator][1] == "CLASS":
                empatar()
                return True
    return False

# Attribute_Definition -> "PRP" "OWN" Attribute_Cycle
def attribute_definition(tokens):
    res = False
    if tokens[iterator][1] == "PRP":
        empatar()
        if tokens[iterator][1] == "OWN":
            empatar()
            res = attribute_cycle(tokens)
    return res

#Attribute_Cycle -> Attribute [ "," Attribute_Cycle ]
def attribute_cycle(tokens):
    res = False
    if attribute(tokens):
        res = True
        if tokens[iterator][1] == ",":
            empatar()
            res = False
            if attribute_cycle(tokens):
                res = True
    return res

# Attribute -> Noun [ "ASSIGN" ( Number | String | Boolean | Pair | Array ) ]
def attribute(tokens):
    res = False
    if noun(tokens):
        res = True
        if tokens[iterator][1] == "ASSIGN":
            empatar()
            if string(tokens) or number(tokens) or boolean(tokens) or pair(tokens) or aray(tokens):
                res = True
            else:
                res = False
    return res

# Functions -> Function_Declarations Function_Definition
def functions(tokens):
    res = False
    if function_declaration(tokens) and function_definition(tokens):
        res = True
    return res

# Function_Declarations -> "PRP" NounCycle
def function_declaration(tokens):
    res = False
    if tokens[iterator][1] == "PRP":
        empatar()
        if noun_cycle(tokens):
            res = True
    return res

# Function_Definition_Cycle -> Function_Definition [ "," Function_Definition_Cycle ]
def function_definition_cicle(tokens):
    res = False
    res = function_definition(tokens)
    if tokens[iterator][1] == ",":
        empatar()
        res = function_definition_cicle(tokens)
    return res

# Function_Definition -> "TO" Noun [Function_Parameters] ( Function_Body | Function_Print) [Function_Definition]
def function_definition(tokens):
    res = False
    if tokens[iterator][1] == "TO":
        empatar()
        if noun(tokens):
            function_parameters(tokens)
            if function_body(tokens) or function_print(tokens):
                res = True
                function_definition(tokens)
    return res

# Function_Parameters -> "PRP" "PARAMVERB" NounCycle
def function_parameters(tokens):
    res = False
    if tokens[iterator][1] == "PRP" and tokens[iterator+1][1] == "PARAMVERB":
        empatar()
        if tokens[iterator][1] == "PARAMVERB":
            empatar()
            if noun_cycle(tokens):
                res = True
    return res

# Function_Print -> "PRP" "PRINT" AnyTokenCycle
def function_print(tokens):
    res = False
    if tokens[iterator][1] == "PRP" and tokens[iterator+1][1] == "PRINT":
        empatar()
        if tokens[iterator][1] == "PRINT":
            empatar()
            res = any_token_cycle(tokens)
    return res

# Function_Body -> FBody_Cycle [ "RETURN" Basic_Type ]
def function_body(tokens):
    res = False
    if f_Body_cycle(tokens):
        res = True
        if tokens[iterator][1] == "RETURN":
            empatar()
            res = basic(tokens)
    return res

# FBody_Cycle -> ( Function_Call | Action ) [ "," FBody_Cycle ]
def f_Body_cycle(tokens):
    res = False
    if function_call(tokens) or action(tokens):
        res = True
        if tokens[iterator][1] == ",":
            empatar()
            if f_Body_cycle(tokens):
                res = True
    return res

# Function_Call -> "PRP" "BODYVERB" Noun [ "PARL" [ Argument_Cycle ] "PARR" ]
def function_call(tokens):
    res = False
    if tokens[iterator][1] == "PRP":
        empatar()
        if tokens[iterator][1] == "BODYVERB":
            empatar()
            if noun(tokens):
                res = True
                if tokens[iterator][1] == "PARL":
                    res = False
                    empatar()
                    argument_cycle(tokens)
                    if tokens[iterator][1] == "PARR":
                        empatar()
                        res = True
    return res

# AnyTokenCycle -> AnyToken [ AnyTokenCycle ]
def any_token_cycle(tokens):
    res = False
    if any_token(tokens):
        res = True
    return res


# AnyToken -> (All tokens until "," or "PTRSTOP")
def any_token(tokens):
    res = True
    while tokens[iterator][1] != "," or tokens[iterator][1] != "PTRSTOP":
        empatar()
    empatar()
    return res

# NounCycle -> Noun [ "," NounCycle ]
def noun_cycle(tokens):
    res = False
    if noun(tokens):
        res = True
        if tokens[iterator][1] == ",":
            empatar()
            res = False
            if noun_cycle(tokens):
                res = True
    return res

# argument_cycle -> Basic_Type [ "," argument_cycle ]
def argument_cycle(tokens):
    res = False
    if basic(tokens):
        res = True
        if tokens[iterator][1] == ",":
            empatar()
            res = argument_cycle(tokens)
    return res

# Action -> "PRP$" Noun ( "ADD" | "SUBS" | "ASSIGN" ) Basic_Type
def action(tokens):
    res = False
    if tokens[iterator][1] == "PRP$":
        empatar()
        if noun(tokens):
            res = True
            if tokens[iterator][1] == "ADD" or tokens[iterator][1] == "SUBS" or tokens[iterator][1] == "ASSIGN":
                empatar()
                if basic(tokens):
                    res = True
    return res

# Basic_Type -> Number | String | Noun | Boolean
def basic(tokens):
    res = False
    if string(tokens) or boolean(tokens) or number(tokens) or noun(tokens):
        res = True
    return res

# Noun -> "NN" | "NNP"
def noun(tokens):
    res = False
    if tokens[iterator][1] == "NNP" or tokens[iterator][1] == "NN":
        empatar()
        res = True
    return res

# String -> "STRSTART [ Content ] STRSTOP"
def string(tokens):
    res = False
    if tokens[iterator][1] == "STRSTART":
        empatar()
        try:
            while(tokens[iterator][1] != "STRSTART"):
                empatar()
        except IndexError:
            return False
        empatar()
        res = True
    return res

# Number -> "CD"
def number(tokens):
    res = False
    if tokens[iterator][1] == "CD":
        empatar()
        res = True
    return res

# Boolean -> "TRUE" | "FALSE"
def boolean(tokens):
    res = False
    if tokens[iterator][1] == "BOOLEAN":
        empatar()
        res = True
    return res

# Pair -> "PARL" "CD" "PARR"
def pair(tokens):
    res = False
    if tokens[iterator][1] == "PARL":
        empatar()
        if tokens[iterator][1] == "CD":
            empatar()
            if tokens[iterator][1] == "PARR":
                empatar()
                res = True
    return res

# Array -> "BRACKL" "CD" "BRACKR"
def aray(tokens):
    res = False
    if tokens[iterator][1] == "BRACKL":
        empatar()
        if number(tokens) and tokens[iterator][1] == "CD":
            empatar()
            if tokens[iterator][1] == "BRACKR":
                empatar()
                res = True
    return res

def sintactico(source):
    name_of_file = source
    tokens  = tokens_from_file(name_of_file)
    return classs(tokens)


if __name__ == "__main__":
    name_of_file = "tokens.txt"
    tokens  = tokens_from_file(name_of_file)
    #access_to_touple(tokens)
    print(tokens)
    #print(tokens[iterador][1])
    print(classs(tokens))


