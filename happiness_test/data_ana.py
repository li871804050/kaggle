import pandas as pd

def read_data(path):
    data = pd.read_csv(path, encoding='gbk')

    if 'happiness' in data.columns:
        data = data[~data['happiness'].isin([-8, -3, -2, -1])]

    drop_list = ['edu_other', 'join_party', 'property_other', 'invest_other', 'survey_time',
                 'nationality', 'religion', 'religion_freq', 'edu_other', 'political', 'floor_area',
                 'property_0', 'property_1', 'property_2', 'property_3', 'property_4', 'property_5', 'property_6',
                 'property_7', 'property_8',
                 'invest_0', 'invest_1', 'invest_2', 'invest_3', 'invest_4', 'invest_5', 'invest_6', 'invest_7',
                 'invest_8',
                 'insur_1', 'insur_2', 'insur_3', 'insur_4',
                 'f_political', 'm_political', 's_political'
                 ]
    data.drop(columns=drop_list, inplace=True)

    heads = data.columns
    stats = []
    for col in heads:
        stats.append((col, data[col].nunique(), data[col].isnull().sum() / data.shape[0], data[col].value_counts(normalize=True, dropna=False).values[0], data[col].dtype))
    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_count', 'NAN_count', 'Max_count', 'type'])


    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 200)

    print(stats_df)



if __name__ == '__main__':
    read_data('data/happiness_train_complete.csv')