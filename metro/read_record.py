import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm

def time_to_type(time):
    ts = time.split(' ')
    td = ts[1].split(':')
    # type = 2
    # if int(td[0]) < 9:
    #     type = 1
    # if int(td[0]) > 18:
    #     type = 3
    time_miu = int(td[0])*60 + int(td[1])
    return int(time_miu/10)

def static_sum(path):
    record = pd.read_csv(path)
    time_to = [time_to_type(x) for x in record['time']]
    # print(time_to)
    record['time'] = time_to
    # record['type'] = time_to[1]
    record['group'] = record['time'].astype(str) + '_' + record['stationID'].astype(str) + '_' + record[
        'status'].astype(str)
    record['count'] = 1
    # record_group = record.groupby(['time', 'stationID', 'status'])
    result = record.groupby('group').sum()
    return result['count']

#时间划分十点以前60 十点到下午五点半之间60到96 五点半之后大于96

if __name__ == '__main__':
    record = static_sum('data/Metro_train/record_2019-01-07.csv')
    y = []
    x = []
    x2 = []
    i = 1
    for r in record.index:
        rs = r.split('_')
        # if int(rs[0]) <= 60:
        #     type = 0
        # elif int(rs[0]) <=
        if int(rs[0]) > 60 and int(rs[0]) > 96 and int(rs[2]) == 1 and int(rs[1]) == 0:
            y.append(record[r])
            x.append(int(rs[0])/10)
            x2.append(int(rs[0])*int(rs[0])/100)
    # print(np.asarray(y).mean(), np.asarray(y).std())
    plt.scatter(x, y)
    plt.show()
    # data = np.asarray([x, x2])
    # print(data.shape)
    # data = data.reshape((40, 2))
    # # print(data)
    # model = sm.OLS(y, data).fit()
    # print(model.summary())

    # plt.scatter(x, y)
    # plt.show()
    # for g in result:
    #     print(g)
    # for i in record_group:
    #     print(i)