from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

def data_deal(path):
    data = pd.read_csv(path, ',', encoding='gbk')

    if 'happiness' in data.columns:
        data = data[~data['happiness'].isin([-8, -3, -2, -1])]
    drop_list = ['edu_other', 'join_party', 'property_other', 'invest_other', 'survey_time',
                 'nationality', 'religion', 'religion_freq', 'edu_other', 'political', 'floor_area',
                 'property_0', 'property_1', 'property_2', 'property_3', 'property_4', 'property_5', 'property_6',
                 'property_7', 'property_8',
                 'invest_0', 'invest_1', 'invest_2', 'invest_3', 'invest_4', 'invest_5', 'invest_6', 'invest_7',
                 'invest_8',
                 'insur_1', 'insur_2', 'insur_3', 'insur_4',
                 'f_political', 'm_political', 's_political',
                 # 'm_birth','f_birth','s_birth','birth','s_income','family_income','income','height_cm','weight_jin',
                 ]
    data.drop(columns=drop_list, inplace=True)

    data.fillna(0, inplace=True)
    return data


def get_dis(a, b):
    SUM = 0
    for i in range(len(a)):
        SUM += pow(a[i] - b[i], 2)
    return SUM

def compare(cents, value):
    cl = 0
    MIN = None
    for i in range(len(cents)):
        dis = get_dis(cents[i], value)
        if  MIN == None or dis < MIN:
            cl = i
            MIN = dis
    return cl + 1


if __name__ == '__main__':
    time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    train_data = data_deal('data/happiness_train_complete.csv')
    data = np.asarray(train_data)
    pro = data[:, 2:]
    target = data[:, 1]

    test_data = data_deal('data/happiness_test_complete.csv')
    t_data = np.asarray(test_data)[:, 1:]
    ids = np.asarray(test_data)[:, 0]
    ST = StandardScaler()
    ST.fit(pro)
    t_data = ST.transform(t_data)
    pro = ST.transform(pro)

    X_TR, X_TS, Y_TR, Y_TS = train_test_split(pro, target, test_size=0.1)

    data_1 = []
    data_2 = []
    data_3 = []
    data_4 = []
    data_5 = []
    for i in range(len(Y_TR)):
        if 1 == Y_TR[i]:
            data_1.append(X_TR[i])
        elif 2 == Y_TR[i]:
            data_2.append(X_TR[i])
        elif 3 == Y_TR[i]:
            data_3.append(X_TR[i])
        elif 4 == Y_TR[i]:
            data_4.append(X_TR[i])
        elif 5 == Y_TR[i]:
            data_5.append(X_TR[i])

    data_1 = np.asarray(data_1)
    data_2 = np.asarray(data_2)
    data_3 = np.asarray(data_3)
    data_4 = np.asarray(data_4)
    data_5 = np.asarray(data_5)
    cnet_1 = np.mean(data_1, 0)
    cnet_2 = np.mean(data_2, 0)
    cnet_3 = np.mean(data_3, 0)
    cnet_4 = np.mean(data_4, 0)
    cnet_5 = np.mean(data_5, 0)
    cnets = [cnet_1, cnet_2, cnet_3, cnet_4, cnet_5]
    PR_Y = []
    for i in range(len(X_TS)):
        PR_Y.append(compare(cnets, X_TS[i]))
    PR_Y = np.asarray(PR_Y)
    print(mean_squared_error(Y_TS, PR_Y))