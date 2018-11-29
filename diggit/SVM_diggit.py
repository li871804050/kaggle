#encode=utf-8

from sklearn.svm import SVC
from diggit import load_data
import numpy as np

if __name__ == '__main__':
    img, label = load_data.deal_train_data(0, 1000)
    clf = SVC(C=4)
    clf.fit(img, label)
    test_img = np.asarray(load_data.train_test[0: 10])
    pre = clf.predict(test_img)
    print(pre)