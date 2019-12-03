import statsmodels.api as sm
import statsmodels.formula.api as smf
spector_data = sm.datasets.spector.load()
family = sm.families.Binomial()
va = sm.cov_struct.Autoregressive()
model = sm.GEE(spector_data.endog, spector_data.exog, spector_data.group, family=family, cov_struct=va)
result = model.fit()
print(result.summary())