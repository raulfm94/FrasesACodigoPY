import nltk
import nltk.tag, nltk.data
from nltk.sem import Valuation, Model


def semantic(paragraph):
    print(paragraph)
    functionDefine = {}
    for sentence in paragraph:
        for value, tag in sentence:
            if tag == "NNP":
                # print value + " tag: " + tag
                functionDefine[value] = +1

        for value, tag in sentence:
            if tag == "NNP":
                if functionDefine[value] <= 2:
                    error = "Error: Function " + value + " is not defined"
                    return error
    return True
