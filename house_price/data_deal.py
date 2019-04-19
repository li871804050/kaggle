import pandas as pd

train_data = pd.read_csv('data/train.csv', index_col=0)
# train_data.fillna(None)

#用None填充空值
cols1 = ["PoolQC" , "MiscFeature", "Alley", "Fence", "FireplaceQu", "GarageQual", "GarageCond", "GarageFinish", "GarageYrBlt", "GarageType", "BsmtExposure", "BsmtCond", "BsmtQual", "BsmtFinType2", "BsmtFinType1", "MasVnrType"]
for col in cols1:
    train_data[col].fillna("None", inplace=True)


#用0填充空值
cols=["MasVnrArea", "BsmtUnfSF", "TotalBsmtSF", "GarageCars", "BsmtFinSF2", "BsmtFinSF1", "GarageArea"]
for col in cols:
    train_data[col].fillna(0, inplace=True)

#用中位数填充
train_data['LotFrontage']=train_data.groupby(['LotAreaCut','Neighborhood'])['LotFrontage'].transform(lambda x: x.fillna(x.median()))