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
    train = np.asarray(train_data)
    train_value = train[: , 0: -1]
    train_pro = train[: , -1: ]
    train_pca_value = train_value
    title = []
    # del_i = [15, 21]
    for i in range(len(train_pca_value[0])):
        if del_i is None:
            title.append(i)
        elif i not in del_i:
            title.append(i)
    train_pca_value = train_pca_value[:, title]

    test_pca_data = np.array(test_data)
    test_pca_data = test_pca_data[:, title]
    return train_pca_value, train_pro, test_pca_data

def data_():
    train = np.asarray(train_data)
    train_value = train[: , 0: -1]
    train_pro = train[: , -1: ].ravel()
    train_pca_value = train_value
    test_pca_data = np.array(test_data)
    return train_pca_value, train_pro, test_pca_data


def loss(x, y):
    pre = net(x)
    losses = tf.reduce_mean(tf.square(y - pre))
    train_step = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(losses)
    # tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return losses, train_step


def net(input):
    logs = tf.layers.dense(inputs=input,
                           units=1,
                           bias_initializer=tf.zeros_initializer(),
                           kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                           kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01),
                           activation=None)
    return logs



def tain(del_i):
    # batch = 256
    if del_i is not None:
        l = 38 - len(del_i)
    else:
        l = 38
    x = tf.placeholder(tf.float32, [None, l], name="input_x")
    y = tf.placeholder(tf.float32, [None, 1], name="output_y")
    pre_value = net(x)
    losses, step = loss(x, y)
    train_pca_value, train_pro, test_pca_data = data(del_i)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for i in range(1000):
            # X_train, X_test, Y_train, Y_test = train_test_split(train_value, train_pro, test_size=0.1, random_state=i)
            X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.2, random_state=i)
            # start = i * batch % len(X_train)
            # end = start + batch
            _,los = sess.run([step, losses], feed_dict={x: X_train, y: Y_train})
            pre_test = sess.run(pre_value, feed_dict={x: X_test})
            pLos = mean_squared_error(Y_test, pre_test)
            print('%d\t%f\t%f'%(i, pLos, los))
        # pre = sess.run(pre_value, feed_dict={x: test_data})
        pre = sess.run(pre_value, feed_dict={x: test_pca_data})
        write = open('data/deep_lasso.txt', 'w')
        for i in range(len(pre)):
            write.write('%f\r'%(pre[i]))
        write.close()

def lassocv_filter():
    model = LassoCV()
    train_value, train_pro, test_value = data_()
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

if __name__ == '__main__':
    del_i = lassocv_filter()
    # del_i = None
    tain(del_i)