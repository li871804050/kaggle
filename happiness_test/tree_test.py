from sklearn.datasets import load_iris
from sklearn import tree
from happiness_test import analyze_data
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
import numpy as np

data = analyze_data.data_deal()

clf = tree.DecisionTreeClassifier()
# col = data.columns.values.tolist()[2: ]
# print(col)
data = np.asarray(data)
pro = data[:, 2:]
target = data[:, 1]
clf = clf.fit(pro, target)

