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

if __name__ == '__main__':
    time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    train_data = analyze_data.data_deal('data/happiness_train_complete.csv')
    data = np.asarray(train_data)
    pro = data[:, 2:]
    target = data[:, 1]

    test_data = analyze_data.data_deal('data/happiness_test_complete.csv')
    t_data = np.asarray(test_data)
    print(len(data[0]))
    ids = t_data[:, 0:1]
    test_pro = t_data[:, 1:]

    X_train, X_test, Y_train, Y_test = train_test_split(pro, target, test_size=0.1, random_state=9)

    #叶子节点所需的最小样本数
    min_leaf = 15
    max_depth = 11
    min_samples_split = 5
    # for max_depth in range(5, 30):
    #     for min_leaf in range(10, 30):
    clf = RandomForestClassifier(n_estimators=30, min_samples_leaf=min_leaf, max_depth=max_depth, min_samples_split=min_samples_split)

    feature_ = BorutaPy(clf, n_estimators='auto', verbose=2, random_state=1, max_iter=max_depth)

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
    # c = 0
    # for i in range(len(Y_PRED)):
    #     # if Y_PRED[i] == Y_test[i]:
    #     c += pow(Y_PRED[i] - Y_test[i], 2)
    # print(c/len(Y_PRED))
    # clf = clf.fit(pro, target)



    predicted = clf.predict(test_pro)

    write = open('data/' + time + ".csv", 'w')
    write.write('id,happiness\r')
    # write2 = open('data/result_20190125_33.csv', 'w')
    for i in range(len(predicted)):
        # print('%d,%d'%(ids[i][0], predicted[i]))
        write.write('%d,%d\r'%(ids[i][0], predicted[i]))
        # write2.write('%d\r'%predicted[i])
    write.close()


    # for n_ne in range(10, 50):
    # kn_clf = KNeighborsClassifier(n_neighbors=10)
    # kn_clf.fit(X_train, Y_train)
    # Y_KN = kn_clf.predict(X_test)
    # ckn = 0
    # for i in range(len(Y_KN)):
    #     if Y_KN[i] == Y_test[i]:
    #         ckn += 1
    # print(ckn/len(Y_KN))

    # ex_tree = ExtraTreesClassifier(n_estimators=50, min_samples_leaf=min_leaf, max_depth=max_depth, min_samples_split=min_samples_split)
    # ex_tree.fit(X_train, Y_train)
    # Y_EX = ex_tree.predict(X_test)
    # cex = 0
    # for i in range(len(Y_EX)):
    #     if Y_EX[i] == Y_test[i]:
    #         cex += 1
    # print(cex/len(Y_EX))

    # PRED_ALL = combain(Y_PRED, Y_KN, Y_EX, Y_test)
    # for i in range(len(Y_EX)):
    #     if PRED_ALL[i] == Y_test[i]:
    #         cex += 1
    # print(cex / len(PRED_ALL))
