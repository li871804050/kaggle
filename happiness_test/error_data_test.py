from sklearn.ensemble import IsolationForest
from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn import tree
from happiness_test import analyze_data
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
import datetime


def combain(x, y, z, t):
    list = []
    for i in range(len(x)):
        value = getMax(x[i], y[i], z[i], t[i])
        list.append(value)
    return list

def getMax(x, y, z, t):
    print(x, y, z, t)
    if y == z:
        return y
    else:
        return x

def error_test(X_data, Y_data):
    error_ = IsolationForest(max_samples=0.99)
    error_.fit(X_data)
    X_ = error_.predict(X_data)
    X_T = []
    Y_T = []
    for i in range(len(X_)):
        if X_[i] == 1:
            X_T.append(X_data[i])
            Y_T.append(Y_data[i])
    return np.asarray(X_T),np.asarray(Y_T)

def LOF_test(X_data,Y_data, j):
    j = j/100
    error_ = LocalOutlierFactor(n_neighbors=40, contamination=j)
    error_.fit(X_data)
    X_ = error_.fit_predict(X_data)
    X_T = []
    Y_T = []
    for i in range(len(X_)):
        if X_[i] == 1:
            X_T.append(X_data[i])
            Y_T.append(Y_data[i])
    return np.asarray(X_T), np.asarray(Y_T)

def OCSVM_test(X_data,Y_data):
    error_ = OneClassSVM()
    error_.fit(X_data)
    X_ = error_.predict(X_data)
    X_T = []
    Y_T = []
    for i in range(len(X_)):
        if X_[i] == -1:
            X_T.append(X_data[i])
            Y_T.append(Y_data[i])
    return np.asarray(X_T), np.asarray(Y_T)

def EE_test(X_data,Y_data,i):
    error_ = EllipticEnvelope(contamination=i)
    error_.fit(X_data)
    X_ = error_.predict(X_data)
    X_T = []
    Y_T = []
    for i in range(len(X_)):
        if X_[i] == 1:
            X_T.append(X_data[i])
            Y_T.append(Y_data[i])
    return np.asarray(X_T), np.asarray(Y_T)

if __name__ == '__main__':
    time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    train_data = analyze_data.data_deal('data/happiness_train_complete.csv')
    data = np.asarray(train_data)

    pro = data[:, 2:]
    target = data[:, 1]

    test_data = analyze_data.data_deal('data/happiness_test_complete.csv')
    t_data = np.asarray(test_data)

    ids = t_data[:, 0:1]
    test_pro = t_data[:, 1:]

    # write = open('data/boruta' + time + ".csv", 'w')
    # for i in range(10, 30):
    #     for j in range(10, 40):
    min_leaf = 18
    max_depth = 14
    min_samples_split = 5
    clf = RandomForestClassifier(n_estimators=30, min_samples_leaf=min_leaf, max_depth=max_depth,
                                 min_samples_split=min_samples_split)
    feature_ = BorutaPy(clf, n_estimators='auto', verbose=2, random_state=1, max_iter=max_depth)
    X_train, X_test, Y_train, Y_test = train_test_split(pro, target, test_size=0.1, random_state=9)
    X_train, Y_train = LOF_test(X_train, Y_train, 7)
    feature_.fit(X_train, Y_train)
    X_train = feature_.transform(X_train)
    X_test = feature_.transform(X_test)
    test_pro = feature_.transform(test_pro)

    clf.fit(X_train, Y_train)
    Y_PRED = clf.predict(X_test)
    loss = mean_squared_error(Y_PRED, Y_test)
    loss_socer = accuracy_score(Y_PRED, Y_test)
    print(loss)
    print(loss_socer)

    #         write.write('%d,%d,%f,%f\r'%(i,j,loss,loss_socer))
    # write.close()




    predicted = clf.predict(test_pro)

    write = open('data/error_' + time + ".csv", 'w')
    write.write('id,happiness\r')
    # write2 = open('data/result_20190125_33.csv', 'w')
    for i in range(len(predicted)):
        # print('%d,%d'%(ids[i][0], predicted[i]))
        write.write('%d,%d\r'%(ids[i][0], predicted[i]))
        # write2.write('%d\r'%predicted[i])
    write.close()

