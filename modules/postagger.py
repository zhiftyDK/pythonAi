import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

def posTagger(sentence):
    tokenized = sent_tokenize(sentence)
    for i in tokenized:
        wordsList = word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        print(tagged)

posTagger("Set a reminder to get my sister in school at 12:30")