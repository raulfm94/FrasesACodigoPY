import nltk
import nltk.tag, nltk.data
from nltk.sem import Valuation, Model


def semantic(paragraph):
    print(paragraph)
    functionDefine = {}
    onString = False
    nextTag = ""
    previusTag = ""
    for sentence in paragraph:
        for value, tag in sentence:
            if tag == "STRSTART":
                onString = True
            if onString == False:
                if nextTag == tag:
                    functionDefine[previusTag] = 2
                    print(functionDefine[previusTag])
                    nextTag = ""
                    previusTag= ""
                else:
                    nextTag = ""
                    previusTag= ""

                if tag == "NNP":
                    if (value in functionDefine) == False:
                        functionDefine[value] = 1
                        nextTag = "ASSIGN"
                        previusTag = value
                    if (value in functionDefine) == True:
                        functionDefine[value] = 2
                        nextTag = "ASSIGN"
                        previusTag = value
            if onString == True:
                if tag == "STRSTART":
                    onString = False

        for value, tag in sentence:
            if tag == "STRSTART":
                onString = True
            if onString == False:
                if tag == "NNP":
                    if functionDefine[value] < 2:
                        error = "Error: Function " + value + " is not defined"
                        print(functionDefine[value])
                        return error
            if onString == True:
                if tag == "STRSTART":
                    onString = False

    return True
