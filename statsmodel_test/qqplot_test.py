import statsmodels.api as sm
from matplotlib import pyplot as plt

import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import plot_ceres_residuals
# data = sm.datasets.longley.load()
# data.exog = sm.add_constant(data.exog)
# mod_fit = sm.OLS(data.endog, data.exog).fit()
# res = mod_fit.resid # residuals
# fig = sm.qqplot(res)
# plt.show()

# crime_data = sm.datasets.statecrime.load_pandas()
# results = smf.ols('murder ~ hs_grad + urban + poverty + single', data=crime_data.data).fit()
# plot_ceres_residuals(results, 'poverty')
# plt.show()

crime_data = sm.datasets.statecrime.load_pandas()
results = smf.ols('murder ~ hs_grad + urban + poverty + single', data=crime_data.data).fit()
sm.graphics.plot_leverage_resid2(results)
plt.show()