#encode=utf-8
import numpy as np
import math
from scipy.stats import f

class line_regression:

    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_ = np.mean(self.x)
        self.y_ = np.mean(self.y)
        self.xy = 0
        self.xx = 0
        self.st = 0
        self.sr = 0
        self.se = 0
        for i in range(len(self.x)):
            self.xy += (self.x[i] - self.x_)*(self.y[i] - self.y_)
            self.xx += (self.x[i] - self.x_)*(self.x[i] - self.x_)
            self.st += (self.y[i] - self.y_) * (self.y[i] - self.y_)
        self.k = self.xy/self.xx
        self.b = self.y_ - self.k * self.x_
        for i in range(len(self.x)):
             self.sr += math.pow(self.k*self.x[i] + self.b - self.y_, 2)
             self.se += math.pow(self.k*self.x[i] + self.b - self.y[i], 2)
        self.f_test = (len(self.x) - 1) * self.sr / self.se





