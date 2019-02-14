from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':

    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    te_data = pd.read_csv('data/zhengqi_test.txt', '\t')
    train_data = np.array(train_data)

    # train_data = train_data.astype('float')
    value = train_data[:, 0:-1]
    target = train_data[:, -1:]

    # clf = LinearDiscriminantAnalysis()


    train_x, test_x, train_y, test_y = train_test_split(value, target, test_size=0.1, random_state=1)
    # model = LinearRegression()
    # print(train_y.shape)
    train_y = train_y.astype('int')
    model = LinearDiscriminantAnalysis()
    model.fit(train_x, train_y)

    pred_y = model.predict(test_x)
    loss = mean_squared_error(pred_y, test_y)
    print(loss)
