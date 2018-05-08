import lexical as lex

input_file = open('input.txt', 'r')
output_file = open('tokens.txt', 'w')
EXAMPLE_TEXT = input_file.read().strip()
input_file.close()
print(EXAMPLE_TEXT)
tokens = lex.lexical(EXAMPLE_TEXT)

for sentence in tokens:
    output_file.write(str(sentence))

output_file.close()