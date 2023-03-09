import pandas as pd
data = pd.read_csv("data-clean3.csv")
data.drop_duplicates(inplace=True) # 删除数据集 data 中的重复行
data.to_csv('data-clean4.csv', index=False)#