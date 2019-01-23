from numpy import random
import numpy as np
from statistics.line import line_regression
import matplotlib.pyplot as plt
from scipy.stats import f
import scipy.special as sp

if __name__ == '__main__':
    x = np.arange(-100, 100, 1)
    ran = random.normal(0, 0.5, len(x))
    y = 5*x + ran - 5
    line = line_regression.line_regression()
    line.fit(x, y)
    print(line.k)
    print(line.b)
    print(line.f_test)
    print(f.cdf(3.89, 1, 200))
    print(f.ppf(0.95, 1, 200))
    print(sp.jn())


