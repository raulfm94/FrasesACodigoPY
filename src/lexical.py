import nltk
import nltk.tag, nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

file = open('input.txt', 'r')
EXAMPLE_TEXT = file.read().strip()
file.close()
print(EXAMPLE_TEXT)
lemma = nltk.wordnet.WordNetLemmatizer()
stop = set(('A', 'a', '.'))
excluded = set(('he', 'she', 'it', 'his', 'her', 'its', 'is', 'and'))
stopWords = set(stopwords.words('english')) - excluded
stopWords.update(stop)

tagger_path = 'taggers/maxent_treebank_pos_tagger/english.pickle'
default_tagger = nltk.data.load(tagger_path)
model = {'To' : 'TO', 'need' : 'PARAMVERB', 'used' : 'BODYVERB', 'increase' : 'ADD', 'decrease': 'SUBS',
         'is' : 'ASSIGN', '``' : 'STRSTART', '\'\'': 'STRSTOP', 'include' : 'OWN', 'own' : 'OWN',
         'possess' : 'OWN', 'have' : 'OWN', '=' : 'ASSIGN', 'True' : 'BOOLEAN', 'False' : 'BOOLEAN',
         'true' : 'BOOLEAN', 'false' : 'BOOLEAN', '(' : 'PARL', ')' : 'PARR', '[' : 'BRACKL', ']' : 'BRACKR',
         'require' : 'PARAMVERB', 'demand' : 'PARAMVERB', 'use' : 'BODYVERB', 'utilize' : 'BODYVERB',
         'exert' : 'BODYVERB', 'employ' : 'BODYVERB', 'wield' : 'BODYVERB', 'apply' : 'BODYVERB',
         'utilized' : 'BODYVERB', 'exerted' : 'BODYVERB', 'employed' : 'BODYVERB', 'wielded' : 'BODYVERB',
         'applied' : 'BODYVERB', 'ha' : 'OWN', 'and' : ',', 'class' : 'CLASS', 'Class' : 'CLASS', 'CLASS' : 'CLASS',
         'return' : 'RETURN', 'Return' : 'RETURN', '0' : 'CD'}
tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)

example_sent = sent_tokenize(EXAMPLE_TEXT)

filtered_sentence = []

for i in range(0, len(example_sent)):
    example_sent[i] = word_tokenize(example_sent[i])

for i in range(0, len(example_sent)):
    for word in example_sent[i]:
        filtered_sentence.append(lemma.lemmatize(word))
    example_sent[i] = filtered_sentence
    filtered_sentence = []

for i in range(0, len(example_sent)):
    for word in example_sent[i]:
        if word not in stopWords:
            filtered_sentence.append(word)
    example_sent[i] = filtered_sentence
    filtered_sentence = []

for i in range(0, len(example_sent)):
    example_sent[i] = tagger.tag(example_sent[i])

for sentence in example_sent:
    print(sentence)