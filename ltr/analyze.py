from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
import gensim
import re
from nltk.corpus import wordnet
import string

porter_stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))
snowball_stemmer = SnowballStemmer("english")

model = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin', binary=True)
# FILTERSTR = "× ℃ ℉ ° φ е ″ Ω".split(" ")

def analyze(sentence):
    word_tokens = word_tokenize(sentence)
    vectors = []
    for w in word_tokens:
        w = snowball_stemmer.stem(w.lower())
        # if w.encode("UTF-8").isalpha():
        #     str = str + w + " "
        # elif w.encode("UTF-8").isdigit():
        #     str = str + "NUM" + " "
        try:
            vectors.append(model[w])
        except(KeyError):
            print(w)
    return vectors



if __name__ == '__main__':
    str = "ET5420 Battery Tester Professional Programmable Dc Electronic Load Battery Indicator Battery Monitor Usb Tестер Charging Tester"
    print(analyze(str))