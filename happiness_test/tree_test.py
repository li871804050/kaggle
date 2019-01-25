from sklearn.datasets import load_iris
from sklearn import tree
from happiness_test import analyze_data
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
import numpy as np

train_data = analyze_data.data_deal('data/happiness_train_complete.csv')

clf = tree.DecisionTreeClassifier()
col = train_data.columns.values.tolist()[2: ]
# print(col)
data = np.asarray(train_data)
pro = data[:, 2:]
target = data[:, 1]
clf = clf.fit(pro, target)

test_data = analyze_data.data_deal('data/happiness_test_complete.csv')
t_data = np.asarray(test_data)
ids = t_data[:,0:1]
test_pro = t_data[:, 1:]

predicted = clf.predict(test_pro)
write = open('data/result_20190125_3.csv', 'w')
write.write('id,happiness\r')
# write2 = open('data/result_20190125_33.csv', 'w')
for i in range(len(predicted)):
    print('%d,%d'%(ids[i][0], predicted[i]))
    write.write('%d,%d\r'%(ids[i][0], predicted[i]))
    # write2.write('%d\r'%predicted[i])
write.close()
# write2.close()
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# tree.export_graphviz(clf, out_file=dot_data,
#                      feature_names=col,
#                      class_names='happiness',
#                      filled=True, rounded=True,
#                      special_characters=True)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph[0].write_pdf("iris.pdf")
# Image(graph[0].create_png())
