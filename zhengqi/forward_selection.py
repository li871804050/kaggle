import statsmodels.formula.api as smf
import pandas as pd


def forward_selected(data, response):
    """前向逐步回归算法，源代码来自https://planspace.org/20150423-forward_selection_with_statsmodels/
    使用Adjusted R-squared来评判新加的参数是否提高回归中的统计显著性
    Linear model designed by forward selection.
    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response
    response: string, name of response column in data
    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()

    return model

if __name__ == '__main__':
    train_data = pd.read_csv('data/zhengqi_train.txt', '\t')
    model = forward_selected(train_data, 'target')

    print(model.model.formula)

    print(model.params)

    print(model.rsquared_adj)

    test_data = pd.read_csv('data/zhengqi_test.txt', '\t')
    print(model.predict(test_data))
