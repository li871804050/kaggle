import pandas as pd
import numpy as np



if __name__ == '__main__':
    train_data = pd.read_csv('data/train.csv', index_col=0)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 200)

    nan_columns = ['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'FireplaceQu']

    heads = train_data.columns
    stats = []
    for col in heads:
        stats.append((col, train_data[col].nunique(), train_data[col].isnull().sum() / train_data.shape[0],
                      train_data[col].value_counts(normalize=True, dropna=False).values[0], train_data[col].dtype))
    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_count', 'NAN_count', 'Max_count', 'type'])
    print(stats_df)