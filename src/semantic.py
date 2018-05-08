import nltk
import nltk.tag, nltk.data
from nltk.sem import Valuation, Model

sentence0 = [('dog', 'NN'), ('is', 'ASSIGN'), ('Class', 'CLASS')]

sentence1 = [('He', 'PRP'), (u'ha', 'OWN'), ('mood', 'NN'), ('=', 'ASSIGN'), ('``', 'STRSTART'), ('HAPPY', 'NNP'), ("''", 'STRSTOP'), (',', ','), ('energy', 'NN'), ('=', 'ASSIGN'), ('100', 'CD'), (',', ','), ('coordenatePosition', 'NNP'), ('=', 'ASSIGN'), ('(', 'PARL'), ('0,0', 'CD'), (')', 'PARR')]

sentence2 = [('He', 'PRP'), ('Bark', 'NNP'), (',', ','), ('Run', 'NNP'), (',', ','), ('MoveLeft', 'NNP'), (',', ','), ('MoveRight', 'NNP'), (',', ','), ('MoveForward', 'NNP'), (',', ','), ('Lay', 'NNP'), ('and', ','), ('Check', 'NNP')]

sentence3 = [('To', 'TO'), ('Run', 'NNP'), ('he', 'PRP'), ('used', 'BODYVERB'), ('MoveForward', 'NNP'), ('(', 'PARL'), ('2', 'CD'), (')', 'PARR'), (',', ','), ('his', 'PRP$'), ('energy', 'NN'), (u'decrease', 'SUBS'), ('1', 'CD'), (',', ','), ('his', 'PRP$'), ('mood', 'NN'), ('is', 'ASSIGN'), ('``', 'STRSTART'), ('PLAY', 'NNP'), ("''", 'STRSTOP'), ('and', ','), ('return', 'RETURN'), ('0', 'CD')]

sentence4 = [('To', 'TO'), ('MoveForward', 'NNP'), ('he', 'PRP'), (u'need', 'PARAMVERB'), ('numbersSteps', 'NNP'), (',', ','), ('his', 'PRP$'), ('coordinatePosition', 'NN'), ('[', 'BRACKL'), ('0', '-NONE-'), (']', 'BRACKR'), (u'increase', 'ADD'), ('numbersSteps', 'NNP'), (',', ','), ('his', 'PRP$'), ('mood', 'NN'), ('is', 'ASSIGN'), ('``', 'STRSTART'), ('MOVING', 'NN'), ("''", 'STRSTOP'), (',', ','), (u'decrease', 'SUBS'), ('energy', 'NN'), ('1', 'CD')]

functionDefine = {}
for value, tag in sentence2:
    if tag == "NNP":
        print value + " tag: " + tag
        functionDefine[value] = False
        print(functionDefine[value])
for value, tag in sentence3:
    if tag == "NNP":
        functionDefine[value] = True
        print(functionDefine[value])

for value, tag in sentence2:
    if tag == "NNP":
        if functionDefine[value] == False:
            print("Error: Function " + value + " is not defined" )
# for value,tag in sentence4:
#     pass




# print("------------------------")
# val = Valuation(sentence1)
# print("Valuation: ",val)
# dom = val.domain
# print("Dom: ",dom)
# g = nltk.sem.Assignment(dom)
# print("G: ",g)
# m = Model(dom, val)
# print("Model: ", m)
# print("Evaluate", m.evaluate('(is & dog & Class)', g))
# print("Evaluate", m.evaluate('He', g))

# val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
# print(val['P'])
# dom = set()
# g = nltk.Assignment(dom)

#
