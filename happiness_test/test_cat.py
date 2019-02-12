import pandas as pd

df2=pd.DataFrame([[1,2,3,4],[2,3,4,5],
                  [3,4,5,6],[4,5,6,7]],
                 index=list('ABCD'),columns=list('ABCD'))
data_3 = df2[df2['A'].isin([1])]
df = pd.concat([df2, data_3])
print(df)