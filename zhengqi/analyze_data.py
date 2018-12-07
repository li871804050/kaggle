#encode=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
train_data = np.array(train_data)
value = train_data[:, 0:-1]
target = train_data[:, -1: ]

def draw_feature(feature):
    length = len(feature)
    x_polt = range(length)
    plt.plot(x_polt, feature)
    plt.show()

if __name__ == '__main__':
    i = 15
    feature = train_data[:, i: i + 1]
    draw_feature(feature)
