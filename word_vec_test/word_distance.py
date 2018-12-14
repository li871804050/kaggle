#encode=utf-8
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def train_vec():
    model = Word2Vec(LineSentence("F:/en_name.txt")
                     ,size=400, window=5, min_count=5)
    model.save("F:/text.model")
    model.wv.save_word2vec_format("F:/text.vector", binary=False)
    print(model.similar_by_word(word='huawei'))
    # print(model.similar_by_vector(vector=))

def use_model():
    model = Word2Vec.load("F:/text.model")
    print(model.similar_by_word(word='huawei'))


if __name__ == '__main__':
    train_vec()
    use_model()