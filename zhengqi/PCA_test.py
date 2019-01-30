import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
te_data = pd.read_csv('data/zhengqi_test.txt', '\t')
train_data = np.array(train_data)

for i in range(10, len(train_data[0] - 1)):
    test_data = te_data
    value = train_data[:, 0:-1]
    target = train_data[:, -1:]
    # print(target)
    # target = [math.log(x) for x in target]
    pca = PCA(n_components=i)
    pca.fit(value)
    # print(pca.singular_values_)
    value = pca.fit_transform(value)
    test_data = pca.fit_transform(test_data)

    train_x, test_x, train_y, test_y = train_test_split(value, target, test_size=0.1, random_state=1)
    model = LinearRegression()
    model.fit(train_x, train_y)

    pred_y = model.predict(test_x)
    loss = mean_squared_error(pred_y, test_y)
    print(i, loss)





