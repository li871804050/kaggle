import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

def read_data():
    path = 'F:\\data\\ali-recommend\\fresh_comp_offline\\tianchi_fresh_comp_train_user.csv'
    table_colums = ['user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category', 'time']
    data = pd.read_csv(path, ',', names=table_colums)
    n_users = data.user_id.unique().shape[0]
    n_items = data.item_id.unique().shape[0]
    print(n_users, n_items)
    train_data = np.zeros((n_users, n_items))
    for line in data:
        train_data[line[0], line[1]] += line[2]
    # 计算用户相似度
    user_similarity = pairwise_distances(train_data, metric='cosine')
    # 计算物品相似度
    item_similarity = pairwise_distances(train_data.T, metric='cosine')
    print(user_similarity)

if __name__ == '__main__':
    read_data()