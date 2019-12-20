import fasttext
from ltr.analyze import analyze


if __name__ == '__main__':
    model = fasttext.train_supervised(input = 'data/train_01.txt', lr=1.0, dim=20, epoch=5, word_ngrams=2, loss='softmax')
    model.save_model('data/01.model')
    # print(model.words)
    # model = fasttext.load_model("data/3.model")
    result = model.test("data/test_01.txt", k=1)
    print(result)
    str = analyze("digit spoon scale kitchen scale food flour weight balanc scale")
    print(model.predict(str, 3))

    # model = fasttext.train_supervised(input='data/train.txt', lr=0.1, dim=100, epoch=5, word_ngrams=2, loss='softmax')
    # model.save_model('data/_1.model')
    # result = model.test_label("data/test_0.txt", k=1)
    # print(result)
    #
    # print(model.predict(str, 3))