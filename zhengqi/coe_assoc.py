import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.nan, suppress=True)

if __name__ == '__main__':
    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    # train_data = np.array(train_data)
    # value = train_data[:, 0:-1]
    # target = train_data[:, -1:]
    # cor = np.corrcoef(train_data)
    # print(cor.shape)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 200)

    pd.set_option('display.width', 1000)
    print(train_data.corr())