import fasttext

if __name__ == '__main__':
    with open("data/news_fasttext_train.txt", "r", encoding="utf-8") as reader:
        sentence = reader.readlines()
        with open("data/new_train.txt", "w", encoding="utf-8") as writer:
            for s in sentence:
                ws = s.split("  ")
                writer.write(ws[0] + "\t" + ws[-1])
            writer.close()
        reader.close()


    model = fasttext.train_supervised(input='data/new_train.txt', lr=0.1, dim=100, epoch=5, word_ngrams=2, loss='softmax')
    # model = fasttext.load_model("data/test.model")
    # result = model.test("data/news_fasttext_test.txt", k=1)
    # print(result)
    # model.save_model("data/test.model")
    print(model.predict("朝鲜 称 完成 对 8000 根乏 燃料 棒 再 处理 "))