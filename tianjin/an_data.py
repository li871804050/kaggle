import pandas as pd
import numpy as np

train = pd.read_csv('data/jinnan_round1_train_20181227.csv', encoding='gbk')

stats = []
for col in train.columns:
    stats.append((col, train[col].nunique(), train[col].isnull().sum() * 100 / train.shape[0],
                  train[col].value_counts(normalize=True, dropna=False).values[0] * 100, train[col].dtype))

stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_values', 'missing',
                                        'Percentage', 'type'])
stats_df.sort_values('Percentage', ascending=False)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

print(stats_df)
# print(train['A5'])