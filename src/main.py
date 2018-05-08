import lexical as lex
import semantic as sem
import sintactico as sintax
import TokensToPythonCode as converter

input_file = open('input.txt', 'r')
output_file = open('tokens.txt', 'w')
EXAMPLE_TEXT = input_file.read().strip()
input_file.close()
print(EXAMPLE_TEXT)
print('Lexical analysis started...\n')
tokens = lex.lexical(EXAMPLE_TEXT)

for sentence in tokens:
    output_file.write(str(sentence))

output_file.close()
print('Lexical analysis finished\n')

print('Syntactic analysis started...\n')
sintax.sintactico('tokens.txt')
print('Syntactic analysis passed.\n')

print('Semantic analysis started...\n')
result = sem.semantic(tokens)
if result is not True:
    print(result)
    quit()
print('Semantic analysis passed.\n')

print('Conversion to code started...\n')
converter.convert_to_code('tokens.txt')
print('Conversion to code finished.\n')

