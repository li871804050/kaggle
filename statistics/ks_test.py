from scipy import stats
import random
import numpy as np

def data():
    norm = []
    for i in range(40):
        c = 0
        for j in range(10):
            c += random.randint(0, 10)
        norm.append(c)
    return norm

def norm_test(data):
    if len(data) < 50:
        p_value = stats.shapiro(data)
        if p_value[1] > 0.05:
            return True
        else:
            return False

def chis():
    stats.chi2.cdf()