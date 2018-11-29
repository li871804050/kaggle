#encode=utf-8
#数据处理 数据填充 重要特征选取


import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier

data_train = pd.read_csv('data/titanic_train.csv', ',')
data_train["Age"] = data_train['Age'].fillna(data_train['Age'].median())
data_train.loc[data_train["Sex"] == "male","Sex"] = 0
data_train.loc[data_train["Sex"] == "female","Sex"] = 1
#缺失值用最多的S进行填充
data_train["Embarked"] = data_train["Embarked"].fillna('S')
#地点用0,1,2
data_train.loc[data_train["Embarked"] == "S","Embarked"] = 0
data_train.loc[data_train["Embarked"] == "C","Embarked"] = 1
data_train.loc[data_train["Embarked"] == "Q","Embarked"] = 2
data_test = pd.read_csv('data/titanic_test.csv', ',')
# df_train = DataFrame(data_train)
# df_test = DataFrame(data_test)

def logisit():
    # print(data_train.info())
    Log = LogisticRegression()
    predictors = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
    predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    re = Log.fit(data_train[predictors], data_train['Survived'])
    scroes = model_selection.cross_val_score(Log, data_train[predictors], data_train['Survived'], cv=3)
    print(scroes.mean())
    data_test["Age"] = data_test["Age"].fillna(data_test["Age"].median())
    # Fare列中的缺失值用Fare最大值进行填充
    data_test["Fare"] = data_test["Fare"].fillna(data_test["Fare"].max())

    # Sex性别列处理：male用0，female用1
    data_test.loc[data_test["Sex"] == "male", "Sex"] = 0
    data_test.loc[data_test["Sex"] == "female", "Sex"] = 1
    # 缺失值用最多的S进行填充
    data_test["Embarked"] = data_test["Embarked"].fillna('S')
    # 地点用0,1,2
    data_test.loc[data_test["Embarked"] == "S", "Embarked"] = 0
    data_test.loc[data_test["Embarked"] == "C", "Embarked"] = 1
    data_test.loc[data_test["Embarked"] == "Q", "Embarked"] = 2

    test_features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    # 构造测试集的Survived列，
    data_test["Survived"] = -1

    test_predictors = data_test[test_features]
    data_test["Survived"] = re.predict(test_predictors)
    print(data_test["Survived"])

def forest():
    predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

    alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
    kf = model_selection.KFold(n_splits=3, shuffle=False, random_state=1)

    scores = model_selection.cross_val_score(alg, data_train[predictors], data_train["Survived"], cv=kf)
    print(scores)
    # Take the mean of the scores (because we have one for each fold)
    print(scores.mean())

if __name__ == '__main__':
    forest()