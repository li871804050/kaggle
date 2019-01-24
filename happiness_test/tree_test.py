from sklearn.datasets import load_iris
from sklearn import tree
from happiness_test import analyze_data
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
import numpy as np

train_data = analyze_data.data_deal('data/happiness_train_abbr.csv')

clf = tree.DecisionTreeClassifier()
# col = data.columns.values.tolist()[2: ]
# print(col)
data = np.asarray(train_data)
pro = data[:, 2:]
target = data[:, 1]
clf = clf.fit(pro, target)

test_data = analyze_data.data_deal('data/happiness_test_abbr.csv')
t_data = np.asarray(test_data)
ids = t_data[:,0:1]
test_pro = t_data[:, 1:]

predicted = clf.predict(test_pro)
write = open('data/result_20190124.csv', 'w')
for i in range(len(predicted)):
    print('%d,%d'%(ids[i][0], predicted[i]))
    write.write('%d,%d\r'%(ids[i][0], predicted[i]))
write.close()

