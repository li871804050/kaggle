
import pandas as pd
import numpy

def read_usr_data(path):
    names = ['user_id', 'gender', 'age', 'buy']
    data = pd.read_csv(path, ',', names=names)
    return data

def read_item(path):
    names = ['product_id', 'cat_id', 'shop_id', 'band_id']
    data = pd.read_csv(path, ',', names=names)
    return data

def read_behavior(path):
    names = ['user_id', 'products_id', 'behav', 'time']
    data = pd.read_csv(path, ',', names=names)
    return data

if __name__ == '__main__':
    path = 'data/train/user.csv'
    read_usr_data(path)
