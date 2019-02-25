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

    pca = PCA()
    pca.fit(pro)
    pro = pca.transform(pro)
    t_data = pca.transform(t_data)

    train_x, test_x, train_y, test_y = train_test_split(pro, target, test_size=0.1, random_state=1)
    # for i in range(3, 30):
    neigh = KNeighborsClassifier(n_neighbors=20, weights='distance')
    neigh.fit(train_x, train_y)

    pre_y = neigh.predict(test_x)
    print(mean_squared_error(pre_y, test_y))


    predict = neigh.predict(t_data)

    writer = open('data/KNN_' + time + '.csv', 'w')
    for i in range(len(ids)):
        writer.write('%d,%d\r'%(ids[i], predict[i]))
