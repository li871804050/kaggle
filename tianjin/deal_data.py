#encoude=utf-8

import pandas as pd

def data():
    data = pd.read_csv('data/jinnan_round1_train_20181227.csv', encoding='gbk')

    time_columns = ['A5', 'A7', 'A9', 'A11', 'A14', 'A16', 'A20', 'A24', 'A26', 'A28', 'B4', 'B5', 'B7', 'B9', 'B10', 'B11']

    #绝大多数数据为空
    data.drop(columns='A2', inplace=True)
    data.drop(columns='A8', inplace=True)
    #时间类型数据暂时不处理
    # data.drop(columns='A5', inplace=True)
    # data.drop(columns='A7', inplace=True)
    # data.drop(columns='A9', inplace=True)
    # data.drop(columns='A11', inplace=True)
    # data.drop(columns='A14', inplace=True)
    # data.drop(columns='A16', inplace=True)
    # data.drop(columns='A20', inplace=True)
    # data.drop(columns='A24', inplace=True)
    # data.drop(columns='A26', inplace=True)
    # data.drop(columns='A28', inplace=True)
    # data.drop(columns='B4', inplace=True)
    # data.drop(columns='B5', inplace=True)
    # data.drop(columns='B7', inplace=True)
    # data.drop(columns='B9', inplace=True)
    # data.drop(columns='B10', inplace=True)
    # data.drop(columns='B11', inplace=True)
    #值基本都是相同
    data.drop(columns='A13', inplace=True)
    data.drop(columns='A18', inplace=True)
    data.drop(columns='A23', inplace=True)
    data.drop(columns='B3', inplace=True)
    data.drop(columns='B13', inplace=True)

    #出现最多的填充空值
    data['A3'].fillna(405, inplace=True)
    data['A21'].fillna(50, inplace=True)
    data['B1'].fillna(320, inplace=True)
    data['B1'].fillna(3.5, inplace=True)
    data['B8'].fillna(45, inplace=True)
    data['B12'].fillna(1200, inplace=True)

    data.fillna(-1, inplace=True)

    heads = data.columns.values.tolist()
    # count = 0
    # data['A5'].fillna(-1, inplace=True)
    # for i in data['A5']:
    #     if i == -1:
    #         count += 1
    # print(count)
    # for t in time_columns:
    data['A20'] = [time_translate_2(x) for x in data['A20']]
    data['A28'] = [time_translate_2(x) for x in data['A28']]
    data['B4'] = [time_translate_2(x) for x in data['B4']]
    data['B9'] = [time_translate_2(x) for x in data['B9']]
    data['B10'] = [time_translate_2(x) for x in data['B10']]
    data['B11'] = [time_translate_2(x) for x in data['B11']]

    data['A5'] = [time_translate(x) for x in data['A5']]
    data['A7'] = [time_translate(x) for x in data['A7']]
    data['A9'] = [time_translate(x) for x in data['A9']]
    data['A11'] = [time_translate(x) for x in data['A11']]
    data['A14'] = [time_translate(x) for x in data['A14']]
    data['A16'] = [time_translate(x) for x in data['A16']]
    data['A24'] = [time_translate(x) for x in data['A24']]
    data['A26'] = [time_translate(x) for x in data['A26']]
    data['B5'] = [time_translate(x) for x in data['B5']]
    data['B7'] = [time_translate(x) for x in data['B7']]

    data['A9-A5'] = tiem_A5(data['A9'], data['A5'])
    data['A11-A9'] = tiem_A5(data['A11'], data['A9'])
    data['A14-A11'] = tiem_A5(data['A14'], data['A11'])
    data['A16-A14'] = tiem_A5(data['A16'], data['A14'])
    data['A24-A16'] = tiem_A5(data['A24'], data['A16'])
    data['A26-A24'] = tiem_A5(data['A26'], data['A24'])
    data['B7-B5'] = tiem_A5(data['B7'], data['B5'])
    for h in heads[1:]:
        data[h] = [y if y > -1.0 else data[h].median() for y in data[h]]

    return data

def time_translate(x):
    if x == -1 or x == '':
        return -1
    str_time = str(x)
    time = str_time.split(':')
    count = 0
    for i in range(len(time)):
        count += int(time[i])*pow(60, 2 - i)
    return count

def time_translate_2(x):
    if x == -1 or x == '':
        return -1
    str_time = str(x)
    # print(x)
    time_ = str_time.split('-')
    count1 = 0
    time0 = time_[0].split(':')
    for i in range(len(time0)):
        count1 += int(time0[i])*pow(60, 2 - i)
    count2 = 0
    time1 = time_[1].split(':')
    for i in range(len(time1)):
        count2 += int(time1[i]) * pow(60, 2 - i)
    t = count2 - count1
    if t < 0:
        t += 24*60*60
    return t/60

def tiem_A5(A7, A5):
    list = []
    for i in range(len(A7)):
        if A7[i] == -1:
            list.append(-1)
        else:
            t = A7[i] - A5[i]
            if (t < 0):
                t += 24*60*60
            list.append(t/60)
    return list

if __name__ == '__main__':
    datas = data()
    # print(data['B10'])
    # print(data['B7-B5'])
    print(datas)