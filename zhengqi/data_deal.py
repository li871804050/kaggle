#encode=utf-8
import pandas as pd
import numpy as np
from sklearn.decomposition import pca


def read_data():
    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    train_data = np.array(train_data)
    value = train_data[:, 0:-1]
    target = train_data[:, -1: ]
    pcas = pca.PCA(n_components=0.95)  # 0.95
    pcas.fit(value)
    X_pca = pcas.transform(value)
    return X_pca, target

def PCA_Data():
    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    train_data = np.array(train_data)
    value = train_data[:, 0: -1]
    pcas = pca.PCA(n_components=0.95)  # 0.95
    pcas.fit(value)
    pca_value = pcas.transform(value)
    return pcas, len(pca_value[0])

def analyze_data(path, spl):
    data = pd.read_csv(path, spl)
    print(data.describe())

def analyze_data_train():
    data = pd.read_csv('data/zhengqi_train.txt', '\t')
    titles = data.columns[0: -1]
    print(data.describe())
    # for t in titles:
    #     des = data[t]
    #     print(des.describe()[2])


if __name__ == '__main__':
    path = 'data/line.txt'
    analyze_data(path, "\t")
    # path = 'data/line.txt'
    # analyze_data(path, "\t")
    # path = 'data/ridge.txt'
    # analyze_data(path, '\t')
    analyze_data_train()
