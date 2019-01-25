#encode=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data_deal(path):
    data = pd.read_csv(path, ',', encoding='gbk')
    remove(data)
    # data.drop(columns=['survey_time'])
    data['birth'] = [get_age_type(x) for x in data['birth']]
    data['height_cm'] = [get_height_type(x) for x in data['height_cm']]
    data['weight_jin'] = [get_weight_type(x) for x in data['weight_jin']]
    data['income'] = [get_income_type(x) for x in data['income']]
    data['family_income'] = [get_income_type(x) for x in data['family_income']]
    data['s_income'] = [get_income_type(x) for x in data['s_income']]
    for i in range(1, 10):
        str_name = 'public_service_' + str(i)
        data[str_name] = [get_service_type(x) for x in data[str_name]]
    return data

def remove(data):
    list = ['province', 'city', 'county', 'survey_time', 'edu_other', 'edu_yr',
            'join_party', 'property_0', 'property_1', 'property_2', 'property_3',
            'property_4', 'property_5', 'property_6', 'property_7', 'property_8',
            'property_other', 'health_problem', 'marital_1st', 's_birth', 'marital_now',
            'f_birth', 'm_birth', 'invest_other']
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

def analyze_birth():
    birth = [2015 - x for x in data['birth']]
    new_age = [get_age_type(x) for x in birth]
    # age = [0 for x in range(100)]
    # for i in range(100):
    #     age[i] = birth.count(i)
    # plt.bar(range(len(age)), age, color='b')
    # age = []
    # for i in range(0, 13):
    #     age.append(new_age.count(i))
    # plt.bar(range(len(age)), age)
    # plt.show()
    return new_age

def get_age_type(age):
    age = 2015 - age
    if age < 20:
        return 0
    elif age >= 80:
        return 13
    else:
        return (age - 20)//5 + 1

def analyze_height():
    height = [x for x in data['height_cm']]
    new_height = [get_height_type(h) for h in height]
    # mn = min(height)
    # mx = max(height)
    # count_height = []
    # # for i in range(mn, mx):
    # #     count_height.append(height.count(i))
    # # plt.bar(range(mn, mx), count_height)
    # # plt.show()
    # new_height = [get_height_type(h) for h in height]
    # for i in range(0, 8):
    #     count_height.append(new_height.count(i))
    # plt.bar(range(0, 8), count_height)
    # plt.show()
    return new_height

def get_height_type(heigh):
    if heigh <= 150:
        return 0
    elif heigh >= 180:
        return 7
    else:
        return (heigh - 150)//5 + 1

def ananlyze_weight():
    weight = [x for x in data['weight_jin']]
    new_weight = [get_weight_type(w) for w in weight]
    return new_weight

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


if __name__ == '__main__':
    path = 'data/happiness_train_complete.csv'
    data = pd.read_csv(path, ',', encoding='gbk')
    analyze_income(data['income'])