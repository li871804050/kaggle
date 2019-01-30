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

def ana_data():
    path = 'data/zhengqi_train.txt'
    train = pd.read_csv(path, '\t')

    stats = []
    for col in train.columns:
        stats.append((col, train[col].nunique(), train[col].isnull().sum() * 100 / train.shape[0],
                      train[col].value_counts(normalize=True, dropna=False).values[0] * 100, train[col].dtype))

    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_values', 'missing',
                                            'Percentage', 'type'])
    stats_df.sort_values('Percentage', ascending=False)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    print(stats_df)

if __name__ == '__main__':
    ana_data()