import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

datas = pd.read_csv('data/happiness_train_complete.csv', encoding='gbk')


def H_W_model(data, n):
    h_w = np.asarray([datas['height_cm'], datas['weight_jin']]).T
    # print(h_w)
    H_W_MODEL = KMeans(n_clusters=n, random_state=1).fit(h_w)

    h_w_test = np.asarray([data['height_cm'], data['weight_jin']]).T
    return H_W_MODEL.predict(h_w_test)


def age_model(data, n):
    b = get_age(datas['birth'])
    s_b = get_age(datas['s_birth'])
    f_b = get_age(datas['f_birth'])
    m_b = get_age(datas['m_birth'])
    birth = np.asarray([b, s_b, f_b, m_b]).T
    AGE_MODEL = KMeans(n_clusters=n, random_state=1).fit(birth)
    b = get_age(data['birth'])
    s_b = get_age(data['s_birth'])
    f_b = get_age(data['f_birth'])
    m_b = get_age(data['m_birth'])
    birth_t = np.asarray([b, s_b, f_b, m_b]).T
    return AGE_MODEL.predict(birth_t)

def income_model(data, n):
    income = datas['income'].fillna(0)
    family_income = datas['family_income'].fillna(0)
    s_income = datas['s_income'].fillna(0)
    income_all = np.asarray([income, family_income, s_income]).T
    INCOME_MODEL = KMeans(n_clusters=n, random_state=2).fit(income_all)

    income = data['income'].fillna(0)
    family_income = data['family_income'].fillna(0)
    s_income = data['s_income'].fillna(0)
    income_all = np.asarray([income, family_income, s_income]).T
    return INCOME_MODEL.predict(income_all)



def get_age(birth):
    age = np.zeros(len(birth))
    for i in range(len(birth)):
        if pd.isna(birth[i]):
            age[i] = -1
        else:
            age[i] = 2015 - birth[i]
    return age



if __name__ == '__main__':
    print()
