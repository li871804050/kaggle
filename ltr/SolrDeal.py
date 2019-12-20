import requests
from pandas.io.json import json_normalize
from ltr.analyze import analyze
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from tensorflow.contrib import learn
import numpy as np
import gensim

cat_paths = 'a6518a a133a a1134a a1091a a155a a1031a a274a a896a a140a a1697a a2006a a3798a a892a a170a'.split(' ')
# cat_paths = 'a6518a a133a a1134a a1091a a155a a1031a a274a'.split(' ')


def getSolrData(keyword):
    url = "http://192.168.4.60:8986/solr/joonmall/select?df=text_all&fl=score,sales7,sales14,sales30,products_price,products_id&q={KEYWORD}&rows=1000&sort=sales30%20desc"
    url = url.replace("{KEYWORD}", keyword)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        docs = data['response']['docs']
        df = json_normalize(docs)
        return df
    return None

def getData():
    url = "http://192.168.4.60:8986/solr/banggood/select?fl=cat_path,products_name_en&q=*:*&rows=10000";
    response = requests.get(url)
    data = response.json()
    return data['response']['docs']

def getData(start, row, cate):
    url = "http://192.168.4.60:8986/solr/banggood/select?fl=products_id,cat_path,products_name_en&q=*:*&start=" + str(start) + "&rows=" + str(row) + "&fq=cat_path:"+ cate
    print(url)
    response = requests.get(url)
    data = response.json()
    return data['response']['docs']

def loadData(user, password, path, start=0, row = 10000):
    sentences = []
    label = []
    with open(path, "w", encoding="gbk") as f:
        for cate in cat_paths:
            datas = getSolrDate(user, password, start, row, cate)
            for data in datas:
                if 'cat_path' in data.keys() and 'products_name_en' in data.keys():
                    value = analyze(data['products_name_en'])
                    print(data["products_id"])
                    print(value + "\t" + "__label__" + cate + "\t" + data["products_id"])
                    sentences.append(value)
                    label.append(cate)
                    f.write(value + "\r")
    f.close()

def loadDataForTF(user, password, start=0, row = 10000):
    sentences = []
    label = []
    max_document_length = 0
    for cate in cat_paths:
        datas = getSolrDate(user, password, start, row, cate)
        for data in datas:
            if 'cat_path' in data.keys() and 'products_name_en' in data.keys():
                value = analyze(data['products_name_en'])
                # print(data["products_id"])
                # print(value + "\t" + "__label__" + cate + "\t" + data["products_id"])
                sentences.append(value)
                label.append(cate)
                max_document_length = max(max_document_length, len(value.split(" ")))
    print(max_document_length)
    vocab_x = learn.preprocessing.VocabularyProcessor(max_document_length)
    x = np.array(list(vocab_x.transform(sentences)))
    vocab_y = learn.preprocessing.VocabularyProcessor(1)
    y = np.array(list(vocab_y.transform(label)))

    # Randomly shuffle data 打乱顺序
    np.random.seed(10)
    shuffle_indices = np.random.permutation(np.arange(len(y)))
    x_shuffled = x[shuffle_indices]
    y_shuffled = y[shuffle_indices]

    x_shuffled = x_shuffled[:, :16]
    dev_sample_index = -1 * int(0.2 * float(len(y)))
    x_train, x_dev = x_shuffled[:dev_sample_index], x_shuffled[dev_sample_index:]
    y_train, y_dev = y_shuffled[:dev_sample_index], y_shuffled[dev_sample_index:]
    return x_train, x_dev, y_train, y_dev

def getSolrDate(user, password, start=0, row=10, cate = ""):
    url = "http://192.168.4.178:8986/solr/banggood/select?fl=products_id,cat_path,products_name_en&q=*:*&start=" + str(
        start) + "&rows=" + str(row) + "&fq=cat_path:" + cate
    a = HTTPBasicAuth(user, password)
    response = requests.get(url, auth=a)
    data = response.json()
    return data['response']['docs']

if __name__ == '__main__':
    user = "solr"
    password = "solr_rocks.18986#_bg"
    # x_train, x_dev, y_train, y_dev = loadDataForTF(user, password, 0, 120)
    # print(x_dev.shape)
    loadData(user, password, "data/test2vec.txt", 0, 12000)
