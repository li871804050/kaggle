import pandas as pd
import numpy as np
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def datas():
    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    train_data = np.array(train_data)
    value = train_data[:, 0:-1]
    target = train_data[:, -1:].ravel()

    # del_i = [27]
    # value = del_zero(del_i, value)
    # del_i = [30]
    # value = del_zero(del_i, value)
    # del_i = [12, 18, 28, 30]
    # value = del_zero(del_i, value)
    return  value, target


def del_zero(del_list, data):
    title = []
    for i in range(len(data[0])):
        if del_list is None or i not in del_list:
            title.append(i)
    data = data[:, title]
    return data

def lasso_test(value, target):
    model = LassoCV()
    X_train, X_test, Y_train, Y_test = train_test_split(value, target, test_size=0.1, random_state=9)
    model.fit(X_train, Y_train)
    pre = model.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    # coef = model.coef_
    # for i in range(len(coef)):
    #     print(i, coef[i])


def line_test(value, target):
    model = LinearRegression()
    X_train, X_test, Y_train, Y_test = train_test_split(value, target, test_size=0.1, random_state=9)
    model.fit(X_train, Y_train)
    pre = model.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    # coef = model.coef_
    # for i in range(len(coef)):
    #     print(i, coef[i])

if __name__ == '__main__':
    value, target = datas()
    lasso_test(value, target)
    line_test(value, target)