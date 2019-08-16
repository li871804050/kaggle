#encode=utf-8
import pandas as pd
import numpy as np
import time
import datetime

item_data = pd.read_csv('data/tianchi_fresh_comp_train_item.csv', ',')
user_data = pd.read_csv('data/tianchi_fresh_comp_train_user.csv', ',')
# item_category 先不适用
# user_geohash
item_fields = ['item_id', 'item_category']
item_data = item_data[item_fields]
user_fields = ['user_id', 'item_id', 'behavior_type', 'item_category', 'time']
user_data = user_data[user_fields]
user_data['time'] = pd.to_datetime(user_data['time'])

# class item_score:
#     def __init__(self, item, time, score):
#         self.item = item
#         self.time = time
#         self.score = score
#
#     def get_hash(self):
#         return hash(self.item) + hash(self.time)
#
#     def get_score(self):
#         return self.score


def get_item_popular_score():
    first_time = user_data['time'].min()
    last_time = user_data['time'].max()
    time_range = pd.date_range(start=first_time, end=last_time, freq='D')
    score_map = {}
    user_data['time'] = [pd.to_datetime(x, '%Y-%m-%d') for x in user_data['time']]
    for i in range(len(time_range)):
        score_item = dict()
        time_data = user_data[user_data['time'] == time_range[i]]
        item_time = time_data['item_id']
        type_time = time_data['behavior_type']
        for j in item_time.keys():
            item = item_time[j]
            type = type_time[j]
            if item in score_item.keys():
                type += score_item[item]
            score_item[item] = type
        if len(score_item) > 0:
            score_map[time_range[i]] = score_item
    return score_map


def get_item_id():
    item_data['item_id']

if __name__ == '__main__':
    # first_time = user_data['time'].min()
    # last_time = user_data['time'].max()
    # time_range = pd.date_range(start=first_time, end=last_time, freq='D')
    # # title = user_data.columns
    # buy = user_data[user_data['behavior_type'] == 4]
    # # print(buy)
    # add = user_data[user_data['behavior_type'] == 3]
    # print(add)
    # user = user_data.groupby('user_id')
    # print(user)
    # print(time_range)
    print(get_item_popular_score())

    item_data = pd.read_csv('data/tianchi_fresh_comp_train_item.csv', ',')
    user_data = pd.read_csv('data/tianchi_fresh_comp_train_user.csv', ',')
    # item_category 先不适用
    # user_geohash
    item_fields = ['item_id', 'item_category']
    item_data = item_data[item_fields]
    user_fields = ['user_id', 'item_id', 'behavior_type', 'time']
    user_data = user_data[user_fields]

    user_data.to_csv('data/user.csv',index=False,header=False)