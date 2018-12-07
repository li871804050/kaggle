#encode=utf-8
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LassoLarsCV
from sklearn.linear_model import ElasticNetCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from zhengqi import data_deal

from statsmodels import regression

train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
test_data = pd.read_csv('data/zhengqi_test.txt', '\t')

def data(del_i = None):
    # PCA_DATA, L = data_deal.PCA_Data()
    train = np.asarray(train_data)
    train_value = train[: , 0: -1]
    train_pro = train[: , -1: ].ravel()
    train_pca_value = train_value
    # train_pca_value = PCA_DATA.transform(train_value)
    title = []
    # del_i = [14, 20]
    for i in range(len(train_pca_value[0])):
        if del_i is None or i not in del_i :
            title.append(i)
    # print(title)
    train_pca_value = train_pca_value[:, title]

    # len_data = len(train_pro)
    test_pca_data = np.array(test_data)
    # test_pca_data = PCA_DATA.transform(test_data)
    test_pca_data = test_pca_data[:, title]
    return train_pca_value, train_pro, test_pca_data

def lassocv_filter():
    model = LassoCV()
    train_value, train_pro, test_value = data()
    X_train, X_test, Y_train, Y_test = train_test_split(train_value, train_pro, test_size=0.1, random_state=9)
    del_i = []
    model.fit(X_train, Y_train)
    pre = model.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)

    cfeo = model.coef_
    for i in range(len(cfeo)):
        if cfeo[i] == 0:
            del_i.append(i)
    print(del_i)
    return del_i

def line_lasso():
    model = LinearRegression()
    del_i = lassocv_filter()
    train_value, train_pro, test_value = data(del_i)
    X_train, X_test, Y_train, Y_test = train_test_split(train_value, train_pro, test_size=0.1, random_state=9)
    model.fit(X_train, Y_train)
    pre = model.predict(X_test)

    loss = mean_squared_error(pre, Y_test)
    print(loss)

    pre_test = model.predict(test_value)
    write = open('data/line_lasso.txt', 'w')
    for i in range(len(pre_test)):
        write.write("%f\r" % pre_test[i])
    write.close()

def line():
    model = LinearRegression()
    # del_i = lassocv_filter()
    train_value, train_pro, test_value = data()
    X_train, X_test, Y_train, Y_test = train_test_split(train_value, train_pro, test_size=0.1, random_state=9)
    model.fit(X_train, Y_train)
    pre = model.predict(X_test)

    loss = mean_squared_error(pre, Y_test)
    print(loss)

    pre_test = model.predict(test_value)
    write = open('data/line_o.txt', 'w')
    for i in range(len(pre_test)):
        write.write("%f\r" % pre_test[i])
    write.close()

if __name__ == '__main__':
    line()
    line_lasso()