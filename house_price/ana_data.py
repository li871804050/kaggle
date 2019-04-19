import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
from scipy.stats import norm


if __name__ == '__main__':
    train_data = pd.read_csv('data/train.csv', index_col=0)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 200)

    # nan_columns = ['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'FireplaceQu']

    # heads = train_data.columns
    # stats = []
    # for col in heads:
    #     stats.append((col, train_data[col].nunique(), train_data[col].isnull().sum() / train_data.shape[0],
    #                   train_data[col].value_counts(normalize=True, dropna=False).values[0], train_data[col].dtype))
    # stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_count', 'NAN_count', 'Max_count', 'type'])
    # print(stats_df)
    # print(train_data.head(5))
    # print(train_data.columns)

    #获取协方差
    train_corr = train_data.corr()
    # print(train_corr)

    # 画出相关性热力图
    # a = plt.subplots(figsize=(20, 12))  # 调整画布大小
    # a = sns.heatmap(train_corr, vmax=.8, square=True)  # 画热力图   annot=True 显示系数
    # plt.show()

    # k = 10  # number of variables for heatmap
    # cols = train_corr.nlargest(k, 'SalePrice')['SalePrice'].index
    # cm = np.corrcoef(train_data[cols].values.T)
    # sns.set(font_scale=1.5)
    # hm = plt.subplots(figsize=(20, 12))  # 调整画布大小
    # hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values,
    #                  xticklabels=cols.values)
    # plt.show()
    #
    sns.set()
    cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    sns.pairplot(train_data[cols], size=2.5)
    plt.show()