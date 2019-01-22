from scipy import constants
import math
from scipy import linalg
import numpy as np
from scipy import stats

if __name__ == '__main__':
    print(math.pi)
    print(constants.pi)
    x = np.array([[1, 3, 5],[2, 5, 1], [2, 3, 8]])
    y = np.array([10, 8, 3])
    z = linalg.solve(x ,y)
    print(z)
    print(linalg.det(x))
    rvs = stats.norm.rvs(loc=5, scale=10, size=(50, 2))
    print(rvs)