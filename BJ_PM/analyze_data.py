import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def draw_data(pro):
    data = pd.read_csv('data/pm25_train.csv')
    pm = data[pro]
    x = range(len(pm))
    plt.plot(x, pm)
    plt.show()

def ana_data():
    data = pd.read_csv('data/pm25_train.csv')
    columns = data.columns
    columns = list(columns)
    # columns.remove('date')
    # columns.remove('hour')
    stats = []
    for col in columns:
        print(col)
        stats.append((col, data[col].nunique(), data[col].isnull().sum() * 100 / data.shape[0],
                      data[col].value_counts(normalize=True, dropna=False).values[0] * 100, data[col].dtype))

    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_values', 'missing',
                                            'Percentage', 'type'])
    stats_df.sort_values('Percentage', ascending=False)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    # print(stats_df)
    print(data.describe())

if __name__ == '__main__':
    ana_data()
    # draw_data('pm2.5')