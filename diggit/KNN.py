#encode=utf-8

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from diggit import load_data

if __name__ == '__main__':
    img, label = load_data.deal_train_data()
    test_data = np.asarray(load_data.train_test)
    # test_label = np.asarray(load_data.test_lable[0: 100])
    nbrs = KNeighborsClassifier(n_neighbors=10, weights='distance')
    nbrs.fit(img, np.ravel(label))
    pre_label = nbrs.predict(test_data)
    print(pre_label)

    with open('data/pro_label.csv', 'w') as writer:
        for i in range(len(pre_label)):
            writer.write(i + "," + pre_label[i] + "\r\n")
        writer.close()