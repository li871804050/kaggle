import numpy as np
import statsmodels.api as sm

spector_data = sm.datasets.spector.load()
#添加常数项
spector_data.exog = sm.add_constant(spector_data.exog, prepend=False)
#因变量(y):  spector_data.endog
#自变量(x):  spector_data.exog
mod = sm.OLS(spector_data.endog, spector_data.exog)
res = mod.fit()
print(res.summary())