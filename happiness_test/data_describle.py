import numpy as np
import pandas as pd

def get_dis_birth(x, y):
    list = []
    for i in range(len(x)):
        list.append(birth_deal(x[i], y[i]))
    return list

def birth_deal(birth, o_birth):
    if o_birth < 0:
        return o_birth
    return  o_birth - birth
    # if pd.isna(bir_dis):
    #     bir_dis = 100
    # elif bir_dis < -40:
    #     bir_dis = -40
    # elif bir_dis > 40:
    #     bir_dis = 40
    # return bir_dis // 5 + 1

if __name__ == '__main__':
    path = 'data/happiness_train_complete.csv'
    data = pd.read_csv(path, ',', encoding='gbk')
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    #通过~取反，选取不包含数字-8的行

    data = data[~data['happiness'].isin([-8, -3, -2, -1])]
    data_3 = data[data['happiness'].isin([1])]
    data = pd.concat([data, data_3])
    data_3 = data[data['happiness'].isin([2])]
    data = pd.concat([data, data_3])
    # print(data['happiness'].describe())
    hp = [x for x in data['happiness']]
    for i in range(1, 6):
        print(hp.count(i))
    print(len(hp))
    # print(data['income'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))
    # data['birth'] = [2015 - x for x in data['birth']]
    # print(data['property_5'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))
    # data['f_birth'] = get_dis_birth(data['birth'], data['f_birth'])
    # print(data['f_birth'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))


