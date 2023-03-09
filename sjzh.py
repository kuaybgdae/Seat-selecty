from sklearn.preprocessing import LabelEncoder
import pandas as pd
df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('data-clean1.csv')
df2['emd_lable2'] = df1['emd_lable2']
df2.to_csv('data-clean2.csv', index=False) # 将emable2加上去
X=pd.read_csv("data-clean2.csv")
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
X_encoded.to_csv("data-clean3.csv", index=False)
