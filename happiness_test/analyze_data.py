#encode=utf-8
import pandas as pd
import matplotlib.pyplot as plt


def data_deal():
    data = pd.read_csv('data/happiness_train_abbr.csv', ',')
    data.drop(columns=['survey_time'], inplace=True)
    data.fillna(-1, inplace=True)
    # data.drop(columns=['survey_time'])
    data['birth'] = [get_age_type(x) for x in data['birth']]
    data['height_cm'] = [x for x in data['height_cm']]
    data['weight_jin'] = [x for x in data['weight_jin']]
    return data


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
    # mn = min(weight)
    # mx = max(weight)
    # count_height = []
    # for i in range(mn, mx):
    #     count_height.append(weight.count(i))
    # plt.bar(range(mn, mx), count_height)
    # plt.show()

def get_weight_type(weigh):
    if weigh <= 50:
        return 0
    elif weigh >= 200:
        return 16
    else:
        return (weigh - 50)//10 + 1

if __name__ == '__main__':
    # analyze_birth()
    # analyze_height()
    data = data_deal()
    print(data.max)