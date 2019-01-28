#encode=utf-8
import numpy as np
import statsmodels.api as sm
from tianjin import deal_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':
    train_datas = np.asarray(deal_data.data('data/jinnan_round1_train_20181227.csv'))
    test_datas = np.asarray(deal_data.data('data/jinnan_round1_testA_20181227.csv'))

    y = train_datas[:, -1: ]
    x = train_datas[:, : -1]
    x = sm.add_constant(x)
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=1)

    model = sm.OLS(train_y, train_x)
    print(train_x.shape)
    print(train_y.shape)
    results = model.fit()
    pred = model.predict(test_x.T)
    print(test_x.shape, pred.shape)
    # loss = mean_squared_error(test_y, pred)
    # print(loss)

    # print(results.summary())
    test_datas = sm.add_constant(test_datas)
    res = model.predict(test_datas.T)
    # print(res)