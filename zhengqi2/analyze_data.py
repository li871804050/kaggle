import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import preprocessing
from sklearn.linear_model import LassoCV,RidgeCV,LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

def deal_data():
    data = pd.read_csv('data/zhengqi_train.txt', '\t')
    columns = data.columns
    # print(columns)
    return data


#前向
def forward_regression(X, y, threshold_in, verbose=False):
    initial_list = []
    included = list(initial_list)
    while True:
        changed=False
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True
            if verbose:
                print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        if not changed:
            break

    return included

#后向
def backward_regression(X, y, threshold_out, included=None, verbose=False):
    if included == None:
        included=list(X.columns)
    while True:
        changed=False
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included


#查看数据整体的情况
def data_describle(data):
    heads = data.columns
    stats = []
    #属性名，取值种类，空值比例，最多相同数据比例，数据类型
    for col in heads:
        stats.append((col, data[col].nunique(), data[col].isnull().sum() / data.shape[0],
                      data[col].value_counts(normalize=True, dropna=False).values[0], data[col].dtype))
    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique_count', 'NAN_count', 'Max_count', 'type'])
    print(stats_df)
    #查看数据的分布情况，均值，方差
    # print(data.describe())

def use_stats_line(data, test_data):
    np_data = np.asarray(data)
    value = np_data[:, -1]
    target = np_data[:, 0: -1]
    #保存训练集中的参数（均值、方差）直接使用其对象转换测试集数据
    scaler_model = preprocessing.StandardScaler().fit(target)
    #axis=0对列进行运算
    #axis=1对行进行运算
    # print(scaler_model.transform(target).mean(axis=0))
    target = scaler_model.transform(target)
    #/kOrdinary Least Squares
    # print(value.shape, target.shape)
    # line_model = sm.OLS(value, target).fit()

    #加权最小二乘拟合 需要设置weight参数
    # line_model = sapi.WLS(value, target).fit()

    #广义最小二乘拟合
    # line_model = sm.GLM(value, target).fit()
    #
    # #递归最小二乘
    # line_model = sm.RecursiveLS(value, target).fit()
    # print(line_model.summary())
    #
    # #lasso回归
    # line_model = LassoCV()
    # line_model.fit(target, value)
    # print(line_model.coef_)
    #
    # #岭回归
    # line_model = RidgeCV()
    # line_model.fit(target, value)
    # print(line_model.coef_)

    data.drop(columns=['target'], inplace=True)

    # 前向回归
    model = forward_regression(X=data, y=value, threshold_in=0.1)
    print(len(model))

    model = backward_regression(X=data, y=value, threshold_out=0.1, included=model)
    print(len(model))
    n_data = data[model]
    n_data = np.asarray(n_data)
    scaler_model = preprocessing.StandardScaler().fit(n_data)
    n_data = scaler_model.transform(n_data)

    t_data = test_data[model]
    t_data = np.asarray(t_data)
    t_data = scaler_model.transform(t_data)
    train_x, test_x, train_y, test_y = train_test_split(data, value, test_size=0.1)


    # line_model = sm.OLS(value, n_data).fit()
    # print(line_model.summary())


    line_model = LinearRegression()
    # line_model.fit(n_data, value)
    line_model.fit(train_x, train_y)
    pred_y = line_model.predict(test_x)
    print(mean_squared_error(test_y, pred_y))

    line_model.fit(n_data, value)
    p_data = line_model.predict(t_data)
    # print(line_model.coef_)
    write = open('data/n_data.txt', 'w')
    for i in range(len(p_data)):
        write.write("%f\r" % p_data[i])
    write.close()



if __name__ == '__main__':
    data = deal_data()
    test_data = pd.read_csv('data/zhengqi_test.txt', '\t')
    use_stats_line(data, test_data)