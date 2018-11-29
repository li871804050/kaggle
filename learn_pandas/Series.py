#encode=utf-8

import numpy as np
import pandas as pd

if __name__ == '__main__':
    arr1 = np.random.permutation(10)
    print(arr1)
    s1 = pd.Series(arr1)
    print(s1.idxmax())
    arr2 = np.array(np.arange(12)).reshape(4, 3)
    df1 = pd.DataFrame(arr2)
    print(df1)