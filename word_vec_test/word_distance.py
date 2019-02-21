#encode=utf-8
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def train_vec():
    model = Word2Vec(LineSentence("F:/en_name2.txt")
                     ,size=400, window=5, min_count=5)
    model.save("F:/text.model")
    model.wv.save_word2vec_format("F:/text.vector", binary=False)
    print(model.similar_by_word(word='huawei'))
    # print(model.similar_by_vector(vector=))

def train_vec2():
    reader = open('F:/words.txt', 'r', encoding='utf-8')
    sentence = []
    for i in reader.readlines():
        str = i[1: -2]
        ws = str.split(', ')
        sentence.append(ws)
    reader.close()
    # print(sentence)
    model = Word2Vec(sentence, min_count=5, size=100)
    model.save("F:/text2.model")
    model.wv.save_word2vec_format("F:/text2.vector", binary=False)
    print(model.similar_by_word(word='huawei'))

def use_model():
    word = 'mi'
    model = Word2Vec.load("F:/text2.model")
    print(model.similar_by_word(word=word))
    model = Word2Vec.load("F:/text.model")
    print(model.similar_by_word(word=word))


if __name__ == '__main__':
    # train_vec2()
    use_model()
    # train_vec()
