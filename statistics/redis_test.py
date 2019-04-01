from __future__ import print_function
import numpy as np
import statsmodels.api as sm
from scipy import stats
from matplotlib import pyplot as plt
from statsmodels.graphics.api import abline_plot
from statsmodels import graphics

data = sm.datasets.star98.load()
data.exog = sm.add_constant(data.exog, prepend=False)
print(data.endog[:5,:])

glm_binom = sm.GLM(data.endog, data.exog, family=sm.families.Binomial())
res = glm_binom.fit()
print(res.summary())

print('Total number of trials:',  data.endog[0].sum())
print('Parameters: ', res.params)
print('T-values: ', res.tvalues)

means = data.exog.mean(axis=0)
means25 = means[:]
means25[0] = stats.scoreatpercentile(data.exog[:,0], 25)
means75 = means[:]
means75[0] = lowinc_75per = stats.scoreatpercentile(data.exog[:,0], 75)
resp_25 = res.predict(means25)
resp_75 = res.predict(means75)
diff = resp_75 - resp_25

print("%2.4f%%" % (diff*100))

nobs = res.nobs
y = data.endog[:,0]/data.endog.sum(1)
yhat = res.mu

fig, ax = plt.subplots()
ax.scatter(yhat, y)
line_fit = sm.OLS(y, sm.add_constant(yhat, prepend=True)).fit()
abline_plot(model_results=line_fit, ax=ax)


ax.set_title('Model Fit Plot')
ax.set_ylabel('Observed values')
ax.set_xlabel('Fitted values')

fig, ax = plt.subplots()

resid = res.resid_deviance[:]
resid_std = stats.zscore(resid)
ax.hist(resid_std, bins=25)
ax.set_title('Histogram of standardized deviance residuals')

graphics.gofplots.qqplot(resid, line='r')

plt.show()