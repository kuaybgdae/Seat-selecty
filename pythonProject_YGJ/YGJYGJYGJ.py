
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出

driver.quit()
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)
from selenium import webdriver
import time

# 创建浏览器对象
# 传入驱动的路径
driver = webdriver.firefox('')
# 访问目标
url = ''
# 访问URL
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 登录按钮
login_text = driver.find_element(By.CSS_SELECTOR,'fl .nologin>a')
# 执行点击操作
login_text.click()
time.sleep(3)
# 用户名输入框
username = driver.find_element(By.ID,'username')
# 输入用户名
username.send_keys('13477934373')
# 输入密
# 安全退出
driver.quit()



import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=5)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
