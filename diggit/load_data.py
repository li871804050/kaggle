#encode=utf-8
from typing import List, Any, Union

import numpy as np
import tensorflow as tf
import pandas as pd
from pandas import Index, Series, DataFrame
from pandas.core.arrays import ExtensionArray
import csv

train_data = pd.read_csv('data/train.csv', ',')
train_test = pd.read_csv('data/test.csv', ',')
test_lable = pd.read_csv('data/sample_submission.csv', ',')
train_len = len(train_data)


def deal_train_data(start = 0, end = train_len):
    data_len = end - start
    start = start % train_len
    end = start + data_len
    if end > train_len:
        start = train_len - data_len
        end = train_len

    data = np.asarray(train_data[start: end])
    data = data.reshape([data_len, 785])
    label = data[: , 0: 1]
    label = np.asarray(label).reshape([data_len, 1])
    img = data[: , 1:]
    img = np.asarray(img).reshape([data_len, 784])
    return img, label


def deal_test_data(start = 0, end = train_len):
    data = np.asarray(train_data)
    return data

if __name__ == '__main__':
    print(train_data.describe())
