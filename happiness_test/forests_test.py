from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn import tree
from happiness_test import analyze_data
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


clf = RandomForestClassifier(n_estimators=35)

train_data = analyze_data.data_deal('data/happiness_train_complete.csv')
data = np.asarray(train_data)
pro = data[:, 2:]
target = data[:, 1]
clf = clf.fit(pro, target)

test_data = analyze_data.data_deal('data/happiness_test_complete.csv')
t_data = np.asarray(test_data)
print(len(data[0]))
ids = t_data[:,0:1]
test_pro = t_data[:, 1:]

X_train, X_test, Y_train, Y_test = train_test_split(pro, target, test_size=0.1, random_state=9)

clf = clf.fit(X_train, Y_train)
Y_PRED = clf.predict(X_test)
loss = mean_squared_error(Y_PRED, Y_test)
print(loss)

# clf = clf.fit(pro, target)

predicted = clf.predict(test_pro)
write = open('data/result_random_tree_20190128_0.csv', 'w')
write.write('id,happiness\r')
# write2 = open('data/result_20190125_33.csv', 'w')
for i in range(len(predicted)):
    # print('%d,%d'%(ids[i][0], predicted[i]))
    write.write('%d,%d\r'%(ids[i][0], predicted[i]))
    # write2.write('%d\r'%predicted[i])
write.close()