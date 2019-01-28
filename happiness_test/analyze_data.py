#encode=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data_deal(path):
    data = pd.read_csv(path, ',', encoding='gbk')

    # data.drop(columns=['survey_time'])
    data['height_cm'] = [get_height_type(x) for x in data['height_cm']]
    data['weight_jin'] = [get_weight_type(x) for x in data['weight_jin']]
    data['income'] = [get_income_type(x) for x in data['income']]
    data['family_income'] = [get_income_type(x) for x in data['family_income']]
    data['s_income'] = [get_income_type(x) for x in data['s_income']]
    data['s_birth'] = get_dis_birth(data['birth'], data['s_birth'])
    data['p_birth'] = get_dis_birth(data['m_birth'], data['f_birth'])
    data['m_birth'] = get_dis_birth(data['birth'], data['f_birth'])
    data['f_birth'] = get_dis_birth(data['birth'], data['f_birth'])
    data['marital_1st'] = get_dis_birth(data['birth'], data['marital_1st'])
    data['marital_now'] = get_dis_birth(data['birth'], data['marital_now'])
    # data['m_birth'] = get_dis_birth(data['birth'], data['m_birth'])
    data['birth'] = [get_age_type(x) for x in data['birth']]
    remove(data)
    for i in range(1, 10):
        str_name = 'public_service_' + str(i)
        data[str_name] = [get_service_type(x) for x in data[str_name]]
    return data

def get_dis_birth(x, y):
    list = []
    for i in range(len(x)):
        list.append(birth_deal(x[i], y[i]))
    return list

def birth_deal(birth, o_birth):
    bir_dis = o_birth - birth
    if pd.isna(bir_dis):
        bir_dis = 100
    elif bir_dis < -40:
        bir_dis = -40
    elif bir_dis > 40:
        bir_dis = 40
    return bir_dis // 5 + 1


def remove(data):
    list = ['province', 'city', 'county', 'survey_time', 'edu_other', 'edu_yr',
            'join_party', 'property_0', 'property_1', 'property_2', 'property_3',
            'property_4', 'property_5', 'property_6', 'property_7', 'property_8',
            'property_other','invest_other']
    # del_null = ['edu_other', 'join_party', 'property_other', 'invest_other']
    # new_deal = ['marital_1st', 'marital_now', 'health_problem']
    heads = data.columns.values.tolist()
    for pro in list:
        if (pro in heads):
            data.drop(columns=[pro], inplace=True)
        else:
            print(pro)
    # data.fillna(-1, inplace=True)
    #缺失值处理
    heads = data.columns.values.tolist()
    for h in heads:
        data[h].fillna(data[h].median(), inplace=True)

# def analyze_birth():
#     birth = [2015 - x for x in data['birth']]
#     new_age = [get_age_type(x) for x in birth]
#     # age = [0 for x in range(100)]
#     # for i in range(100):
#     #     age[i] = birth.count(i)
#     # plt.bar(range(len(age)), age, color='b')
#     # age = []
#     # for i in range(0, 13):
#     #     age.append(new_age.count(i))
#     # plt.bar(range(len(age)), age)
#     # plt.show()
#     return new_age

def get_age_type(age):
    age = 2015 - age
    if age < 20:
        return 0
    elif age >= 80:
        return 13
    else:
        return (age - 20)//5 + 1

# def analyze_height():
#     height = [x for x in data['height_cm']]
#     new_height = [get_height_type(h) for h in height]
#     # mn = min(height)
#     # mx = max(height)
#     # count_height = []
#     # # for i in range(mn, mx):
#     # #     count_height.append(height.count(i))
#     # # plt.bar(range(mn, mx), count_height)
#     # # plt.show()
#     # new_height = [get_height_type(h) for h in height]
#     # for i in range(0, 8):
#     #     count_height.append(new_height.count(i))
#     # plt.bar(range(0, 8), count_height)
#     # plt.show()
#     return new_height

def get_height_type(heigh):
    if heigh <= 150:
        return 0
    elif heigh >= 180:
        return 7
    else:
        return (heigh - 150)//5 + 1

# def ananlyze_weight():
#     weight = [x for x in data['weight_jin']]
#     new_weight = [get_weight_type(w) for w in weight]
#     return new_weight

def get_weight_type(weigh):
    if weigh <= 50:
        return 0
    elif weigh >= 200:
        return 16
    else:
        return (weigh - 50)//10 + 1

def analyze_income(data):
    income = [x for x in data]
    draw_data_fq(income)

def get_income_type(income):
    # print(type(income), income)
    if income < 10000:
        return 0
    elif income >= 10000 and income < 50000:
        return 1
    elif income >= 50000 and income < 100000:
        return 2
    elif income >= 100000 and income < 200000:
        return 3
    elif income >= 200000 and income < 500000:
        return 4
    elif income >= 500000 and income < 1000000:
        return 5
    elif income >= 1000000:
        return 6

def draw_data_fq(datas):
        mn = min(datas)
        mx = max(datas)
        print(mn,mx)
        # count_height = []
        # for i in range(mn, mx):
        #     count_height.append(datas.count(i))
        # plt.bar(range(mn, mx), count_height)
        # plt.show()

def get_service_type(data):
    return data//10;


def ana_data():
    list = ['province', 'city', 'county', 'survey_time', 'edu_other', 'edu_yr',
            'join_party', 'property_0', 'property_1', 'property_2', 'property_3',
            'property_4', 'property_5', 'property_6', 'property_7', 'property_8',
            'property_other', 'health_problem', 'marital_1st', 'marital_now',
            'invest_other']

    path = 'data/happiness_train_complete.csv'
    train = pd.read_csv(path, ',', encoding='gbk')
    stats = []
    for col in list:
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

# if __name__ == '__main__':
#     path = 'data/happiness_train_complete.csv'
#     data = pd.read_csv(path, ',', encoding='gbk')
#     print(data['marital_now'])
