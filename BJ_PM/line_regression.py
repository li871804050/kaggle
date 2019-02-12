import statsmodels.api as sm
import pandas as pd
import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error


def line_stas():
    data = pd.read_csv('data/pm25_train.csv')
    # print(data['pm2.5'])
    target = [x for x in data['pm2.5']]
    data.drop(columns=['date'], inplace=True)
    data = np.asarray(data, dtype=float)
    pro = data[: , 2:]
    # clf = sm.OLS(target, pro)
    clf = sm.GLM(target, pro)
    res = clf.fit()
    print(res.summary())

def line_regression():
    data = pd.read_csv('data/pm25_train.csv')
    # print(data['pm2.5'])
    target = [x for x in data['pm2.5']]
    data.drop(columns=['date'], inplace=True)
    data = np.asarray(data, dtype=float)
    pro = data[:, 2:]
    X_, X_T, Y_, Y_T = train_test_split(pro, target, test_size=0.01, random_state=1)
    clf = LinearRegression()
    # clf = LassoCV()
    clf.fit(X_, Y_)
    Y_P = clf.predict(X_T)
    loss = mean_squared_error(Y_P, Y_T)
    print(len(Y_T))
    print(loss)

if __name__ == '__main__':
    # line_stas()
    line_regression()