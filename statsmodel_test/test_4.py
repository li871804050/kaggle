import statsmodels.api as sm
import numpy as np
from statsmodels.gam.api import GLMGam, BSplines
from statsmodels.gam.tests.test_penalized import df_autos
x_spline = df_autos[['weight', 'hp']]
bs = BSplines(x_spline, df=[12, 10], degree=[3, 3])
alpha = np.array([21833888.8, 6460.38479])
gam_bs = GLMGam.from_formula('city_mpg ~ fuel + drive', data=df_autos,
                             smoother=bs, alpha=alpha)

res_bs = gam_bs.fit()
print(res_bs.summary())
res_bs.plot_partial(0, cpr=True)
res_bs.plot_partial(1, cpr=True)
alpha = np.array([8283989284.5829611, 14628207.58927821])
gam_bs = GLMGam.from_formula('city_mpg ~ fuel + drive', data=df_autos,
                             smoother=bs, alpha=alpha,
                             family=sm.families.Poisson())

res_bs = gam_bs.fit()
print(res_bs.summary())
gam_bs.select_penweight()[0]
gam_bs.select_penweight_kfold()[0]