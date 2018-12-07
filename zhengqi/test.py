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
# PCA_DATA, L = data_deal.PCA_Data()
train = np.asarray(train_data)
train_value = train[: , 0: -1]
train_pro = train[: , -1: ].ravel()
train_pca_value = train_value
# train_pca_value = PCA_DATA.transform(train_value)
title = []
del_i = [14, 20]
for i in range(len(train_pca_value[0])):
    if i not in del_i :
        title.append(i)
# print(title)
train_pca_value = train_pca_value[:, title]

len_data = len(train_pro)
test_data = np.array(test_data)
test_pca_data = test_data
# test_pca_data = PCA_DATA.transform(test_data)
test_pca_data = test_pca_data[:, title]


def get_data(start, betch):
    start = start%len_data
    end = start + betch
    if end  <= len_data:
        return train_pro[start: end], train_value[start: end]
    else:
        end = end%len_data
        pro_n = np.vstack((train_pro[0: end], train_pro[start:]))
        value_n = np.vstack((train_value[: end], train_value[start:]))
        return pro_n, value_n


def net(input):
    logs = tf.layers.dense(inputs=input,
                           units=1,
                           bias_initializer=tf.zeros_initializer(),
                           kernel_regularizer=tf.contrib.layers.l2_regularizer(0.001),
                           activation=None)
    return logs

def loss(x, y):
    pre = net(x)
    losses = tf.reduce_mean(tf.square(y - pre))
    train_step = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(losses)
    # tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return losses, train_step

def tain(l):
    # batch = 256
    x = tf.placeholder(tf.float32, [None, l], name="input_x")
    y = tf.placeholder(tf.float32, [None, 1], name="output_y")
    pre_value = net(x)
    losses, step = loss(x, y)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for i in range(10000):
            # X_train, X_test, Y_train, Y_test = train_test_split(train_value, train_pro, test_size=0.1, random_state=i)
            X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=i)
            # start = i * batch % len(X_train)
            # end = start + batch
            _,los = sess.run([step, losses], feed_dict={x: X_train, y: Y_train})
            pre_test = sess.run(pre_value, feed_dict={x: X_test})
            pLos = mean_squared_error(Y_test, pre_test)
            print('%d\t%f'%(i, pLos))
        # pre = sess.run(pre_value, feed_dict={x: test_data})
        pre = sess.run(pre_value, feed_dict={x: test_pca_data})
        write = open('data/deep.txt', 'w')
        for i in range(len(pre)):
            write.write('%f\r'%(pre[i]))
        write.close()

def line():
    line = LinearRegression()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    line.fit(X_train, Y_train)

    pre = line.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = line.predict(test_pca_data)
    write = open('data/line.txt', 'w')
    for i in range(len(pre)):
        write.write ("%f\r"%pre[i])
    write.close()

def ridge():
    ridge = RidgeCV()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    ridge.fit(X_train, Y_train)
    pre = ridge.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = ridge.predict(test_pca_data)
    write = open('data/ridge.txt', 'w')
    for i in range(len(pre)):
        write.write ("%f\r"%pre[i])
    write.close()

def lassocv():
    lasso = LassoCV()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    lasso.fit(X_train, Y_train)
    pre = lasso.predict(X_test)
    loss = mean_squared_error(pre, Y_test)

    print(loss)
    # print(lasso.coef_)
    coef = lasso.coef_
    for i in range(len(coef)):
        if (coef[i] == 0):
            print("%d\t%f"%(i, coef[i]))
    # print(lasso.alpha_)
    # print(lasso.dual_gap_)
    # print(lasso.n_iter_)
    # pre = lasso.predict(test_pca_data)
    # write = open('data/lasso.txt', 'w')
    # for i in range(len(pre)):
    #     write.write ("%f\r"%pre[i])
    # write.close()

def elasticnet():
    elasticnet = ElasticNetCV()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    elasticnet.fit(X_train, Y_train)
    pre = elasticnet.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = elasticnet.predict(test_pca_data)
    write = open('data/elasticnet.txt', 'w')
    for i in range(len(pre)):
        write.write("%f\r" % pre[i])
    write.close()

def lassolars():
    lassolars = LassoLarsCV()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    lassolars.fit(X_train, Y_train)
    pre = lassolars.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = lassolars.predict(test_pca_data)
    write = open('data/lassolars.txt', 'w')
    for i in range(len(pre)):
        write.write("%f\r" % pre[i])
    write.close()

def grad():
    grad = GradientBoostingRegressor()
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    grad.fit(X_train, Y_train)
    pre = grad.predict(X_test)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = grad.predict(test_pca_data)
    write = open('data/grad.txt', 'w')
    for i in range(len(pre)):
        write.write("%f\r" % pre[i])
    write.close()

def polyomial():
    poly = PolynomialFeatures(degree=2)
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=9)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.fit_transform(X_test)
    test_pca_data_poly = poly.fit_transform(test_pca_data)
    regressor_poly = LassoLarsCV()
    regressor_poly.fit(X_train_poly, Y_train)
    pre = regressor_poly.predict(X_test_poly)
    loss = mean_squared_error(pre, Y_test)
    print(loss)
    pre = regressor_poly.predict(test_pca_data_poly)
    write = open('data/poly.txt', 'w')
    for i in range(len(pre)):
        write.write("%f\r" % pre[i])
    write.close()


if __name__ == '__main__':
    line()
    polyomial()
    # grad()
    # ridge()
    # lassocv()
    # lassolars()
    # elasticnet()