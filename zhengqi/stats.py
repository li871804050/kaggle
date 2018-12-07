#encode=utf-8

import statsmodels.api as sm
import pandas as pd
import numpy as np
from zhengqi import data_deal
from sklearn.model_selection import train_test_split

train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
test_data = pd.read_csv('data/zhengqi_test.txt', '\t')
PCA_DATA, L = data_deal.PCA_Data()
train = np.asarray(train_data)
train_value = train[: , 0: -1]
train_pro = train[: , -1: ].ravel()
train_pca_value = train_value
# train_pca_value = PCA_DATA.transform(train_value)
# print(len(train_pca_value[0]))
# title = []
# del_i = [5, 6, 10, 13, 15]
# for i in range(len(train_pca_value[0])):
#     if i not in del_i :
#         title.append(i)
# print(title)
# train_pca_value = train_pca_value[:, title]

test_data = np.array(test_data)
test_pca_data = test_data
# test_pca_data = PCA_DATA.transform(test_data)
# test_pca_data = test_pca_data[:, title].T
test_pca_data = test_pca_data.T

if __name__ == '__main__':
    X_train, X_test, Y_train, Y_test = train_test_split(train_pca_value, train_pro, test_size=0.1, random_state=20)
    # sm.OLS.fit_regularized(L1_wt=1)
    model = sm.OLS(Y_train, X_train)
    result = model.fit_regularized()
    result = model.fit()
    print(result.params)
    print(result.summary())
    pre_data = model.predict(test_pca_data)
    write = open('data/stats.txt', 'w')
    for i in range(len(pre_data[0])):
        write.write("%f\r" % pre_data[0][i])
    write.close()