import gensim, logging
from gensim.models.word2vec import LineSentence

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# train word2vec on the two sentences
model = gensim.models.Word2Vec(LineSentence("data/test2vec.txt"), min_count=5)
model.save("data/vec.model")
print(model[["usb", "electr", "wood"]].shape)