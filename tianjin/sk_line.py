from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tianjin import deal_data
import pandas as pd
import numpy as np
import statsmodels.api as sm

clf = linear_model.LinearRegression()

train_datas = np.asarray(deal_data.data('data/jinnan_round1_train_20181227.csv'))
test_datas = np.asarray(deal_data.data('data/jinnan_round1_testA_20181227.csv'))
ids = pd.read_csv('data/jinnan_round1_testA_20181227.csv', encoding='gbk')['样本id']

y = train_datas[:, -1:]
# y = [x for x in y]
x = train_datas[:, : -1]

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=1)

clf = linear_model.LinearRegression()
clf.fit(train_x, train_y)

pred_y = clf.predict(test_x)
loss = mean_squared_error(test_y, pred_y)
print(loss)

pred_test = clf.predict(test_datas)
write = open('data/res_20190128.csv', 'w')
for i in range(len(pred_test)):
    write.write('%s,%f\r'%(ids[i], pred_test[i]))
write.close()


# model = sm.OLS(train_y, train_x)
# results = model.fit()
# print(train_x.shape)
# print(train_y.shape)
# pred = model.predict(test_x)
#
# # print(test_x.shape, pred.shape)
# loss = mean_squared_error(test_y, pred)
# print(loss)