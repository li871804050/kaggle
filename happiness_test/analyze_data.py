#encode=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data_deal(path):
    data = pd.read_csv(path, ',', encoding='gbk')

    # data.drop(columns=['survey_time'])
    if 'happiness' in data.columns:
        data = data[~data['happiness'].isin([-8, -3, -2, -1])]
        # data_3 = data[data['happiness'].isin([1])]
        # data = pd.concat([data, data_3, data_3, data_3])
        # data_3 = data[data['happiness'].isin([2])]
        # data = pd.concat([data, data_3])
    data['BMI'] = get_BMI(data['height_cm'], data['weight_jin'])
    data['height_cm'] = [get_height_type(x) for x in data['height_cm']]
    data['weight_jin'] = [get_weight_type(x) for x in data['weight_jin']]
    data['income'] = [get_income_type(x) for x in data['income']]
    data['family_income'] = [get_income_type(x) for x in data['family_income']]
    data['s_income'] = [get_income_type(x) for x in data['s_income']]
    data['s_b'] = sbirth_deal(data['birth'], data['s_birth'])
    data['p_b'] = sbirth_deal(data['m_birth'], data['f_birth'])
    data['m_b'] = get_dis_birth(data['birth'], data['f_birth'])
    data['f_b'] = get_dis_birth(data['birth'], data['f_birth'])
    data['marital_1st'] = get_dis_birth(data['birth'], data['marital_1st'])
    data['marital_now'] = get_dis_birth(data['birth'], data['marital_now'])

    # data['m_birth'] = get_dis_birth(data['birth'], data['m_birth'])
    data['birth'] = [get_age_type(x) for x in data['birth']]
    data['s_birth'] = [get_age_type(x) for x in data['s_birth']]
    data['f_birth'] = [get_age_type(x) for x in data['f_birth']]
    data['m_birth'] = [get_age_type(x) for x in data['m_birth']]
    # remove(data)
    drop_list = ['edu_other', 'join_party', 'property_other', 'invest_other', 'survey_time',
                 'nationality', 'religion', 'religion_freq', 'edu_other', 'political', 'floor_area',
                 'property_0', 'property_1', 'property_2', 'property_3', 'property_4', 'property_5', 'property_6',
                 'property_7', 'property_8',
                 'invest_0', 'invest_1', 'invest_2', 'invest_3', 'invest_4', 'invest_5', 'invest_6', 'invest_7',
                 'invest_8',
                 'insur_1', 'insur_2', 'insur_3', 'insur_4',
                 'f_political', 'm_political', 's_political'
                 ]
    data.drop(columns=drop_list, inplace=True)

    data.fillna(-3, inplace=True)
    for i in range(1, 10):
        str_name = 'public_service_' + str(i)
        data[str_name] = [get_service_type(x) for x in data[str_name]]
    return data

def get_dis_birth(x, y):
    list = []
    x = np.asarray(x)
    y = np.asarray(y)
    for i in range(len(x)):
        list.append(birth_deal(y[i], x[i]))
    return list

def sbirth_deal(x, y):
    list = []
    x = np.asarray(x)
    y = np.asarray(y)
    for i in range(len(x)):
        if y[i] < 0 or x[i] < 0:
            list.append(min(y[i],x[i])*100)
        else:
            bir_dis = x[i] - y[i]
            if pd.isna(bir_dis):
                list.append(100)
            elif bir_dis < -4:
                list.append(-5)
            elif bir_dis > 4:
                list.append(5)
            else:
                list.append( bir_dis)
    return list

def birth_deal(birth, o_birth):
    if o_birth < 0 or birth < 0:
        return min(o_birth, birth)*100
    bir_dis = o_birth - birth
    if pd.isna(bir_dis):
        return 100
    elif bir_dis < 20:
        return 0
    elif bir_dis < 25:
        return 1
    elif bir_dis < 30:
        return 2
    elif bir_dis < 35:
        return 3
    else:
        return 4


def remove(data):
    list = ['province', 'city', 'county', 'survey_time', 'edu_other', 'edu_yr', 'join_party',
            'property_0', 'property_1', 'property_2', 'property_3', 'property_4', 'property_5', 'property_6', 'property_7', 'property_8',
            'property_other','invest_other']
    # del_null = ['edu_other', 'join_party', 'property_other', 'invest_other']
    # new_deal = ['marital_1st', 'marital_now', 'health_problem']
    heads = data.columns.values.tolist()
    for pro in list:
        if (pro in heads):
            data.drop(columns=[pro], inplace=True)
        else:
            print(pro)
    data.fillna(-3, inplace=True)
    #缺失值处理
    # heads = data.columns.values.tolist()
    #     # for h in heads:
    #     #     data[h].fillna(data[h].median(), inplace=True)

def get_age_type(age):
    if age < 0:
        return age
    elif pd.isna(age):
        return 100
    age = 2015 - age
    if age < 25:
        return 0
    elif age < 35:
        return 1
    elif age < 45:
        return 2
    elif age < 55:
        return 3
    elif age < 65:
        return 4
    elif age < 75:
        return 5
    else:
        return 6

def get_height_type(heigh):
    if pd.isna(heigh):
        return -1
    if heigh < 0:
        return heigh
    if heigh <= 150:
        return 0
    elif heigh >= 180:
        return 7
    else:
        return (heigh - 150)//5 + 1

def get_weight_type(weigh):
    if pd.isna(weigh):
        return -1

    if weigh < 0:
        return weigh

    if weigh <= 80:
        return 0
    elif weigh >= 150:
        return 8
    else:
        return (weigh - 80)//10 + 1

def get_income_type(income):
    # print(type(income), income)
    if pd.isna(income):
        return -1
    if income < 0:
        return income
    if income < 10:
        return income
    if income <= 3000:
        return 0
    elif income <= 10000:
        return 1
    elif income <= 20000:
        return 2
    elif income <= 30000:
        return 3
    elif income <= 40000:
        return 4
    elif income <= 600000:
        return 6
    else:
        return 7
def get_service_type(data):
    if data < 0:
        return data
    return data//10;


def ana_data():
    # list = ['province', 'city', 'county', 'survey_time', 'edu_other', 'edu_yr',
    #         'join_party',
    #         # 'property_4', 'property_5', 'property_6', 'property_7', 'property_8','property_0', 'property_2', 'property_3',
    #         'property_other', 'invest_other']

    path = 'data/happiness_train_complete.csv'
    train = pd.read_csv(path, ',', encoding='gbk')
    head = train.columns
    stats = []
    for col in head:
        stats.append((col, train[col].nunique(), train[col].isnull().sum() * 100 / train.shape[0],
                      train[col].value_counts(normalize=True, dropna=False).values[0] * 100, train[col].dtype))

    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_values', 'missing',
                                            'Percentage', 'type'])
    stats_df.sort_values('Percentage', ascending=False)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    print(stats_df)

def get_BMI(heighs, weights):
    list = []
    heighs = np.asarray(heighs)
    weights = np.asarray(weights)
    for i in range(len(heighs)):
        # if pd.isna(weight[i]) or pd.isna(heighs[i]):
        #     list.append(-1)
        #     continue

        weight = weights[i]/2
        heigh = heighs[i]/100
        if heigh == 0:
            list.append(-1)
            continue
        bmi = weight/(heigh*heigh)
        if bmi < 18.5:
            list.append(0)
        elif bmi < 25:
            list.append(1)
        elif bmi < 30:
            list.append(2)
        elif bmi < 35:
            list.append(3)
        else:
            list.append(4)
    # print(list)
    return list

# if __name__ == '__main__':
#     path = 'data/happiness_train_complete.csv'
#     data = pd.read_csv(path, ',', encoding='gbk')
#     print(data['property_1'])
    # ana_data()
