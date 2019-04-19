import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 200)

#设置第0行为索引
train = pd.read_csv('data/train.csv', index_col=0)
test = pd.read_csv('data/test.csv')

# 返回每列列名,该列非nan值个数,以及该列类型
# print(train.info())
#返回数据的均值方差和分位数
# print(train.describe(percentiles=[0.00, 0.25, 0.50, 0.75, 1.00]))

print(train['Survived'].value_counts())

# train_corr = train.corr()
# # 画出相关性热力图
# a = plt.subplots(figsize=(20, 12))  # 调整画布大小
# # 画热力图   annot=True 显示系数vmin,vmax最小值和最大值
# a = sns.heatmap(train_corr,vmin=-1.0, vmax=1.0, square=True, annot=True)
# plt.show()

print(train[['Pclass','Survived']].groupby(['Pclass']).mean())
print(train[['Sex','Survived']].groupby(['Sex']).mean())
print(train[['SibSp','Survived']].groupby(['SibSp']).mean())


