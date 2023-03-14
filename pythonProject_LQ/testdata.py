import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
# 加载训练好的模型
from sklearn.preprocessing import LabelEncoder, StandardScaler
model = tf.keras.models.load_model('./my_model.h5')
# 加载测试数据
test_data = pd.read_csv('test.csv',dtype={57: str, 147: str, 142: str})
test_data.head() # 查看前几行数据
test_data.describe() # 查看数据的统计信息
test_data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
test_data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行

encoder = LabelEncoder()
for col in test_data.select_dtypes(include='object'):
    test_data[col] = encoder.fit_transform(test_data[col].astype(str))

select_features=['seg_route_to', 'seg_flight', 'seg_cabin', 'pax_fcny', 'emd_lable',
       'gender', 'cabin_c_cnt_y1', 'cabin_c_cnt_y2', 'cabin_c_cnt_y3',
       'pref_aircraft_y1_3', 'pref_aircraft_y1_4', 'pref_aircraft_y1_5',
       'pref_aircraft_y2_1', 'pref_aircraft_y2_2', 'pref_aircraft_y2_3',
       'pref_aircraft_y2_4', 'pref_aircraft_y2_5', 'pref_aircraft_y3_1',
       'pref_aircraft_y3_2', 'pref_aircraft_y3_3', 'pref_aircraft_y3_4',
       'pref_aircraft_y3_5', 'seat_middle_cnt_m3', 'pref_city_y2_1',
       'dist_cnt_y3', 'avg_dist_cnt_y2', 'avg_dist_cnt_y3',
       'select_seat_cnt_y1', 'select_seat_cnt_y2', 'select_seat_cnt_y3',
       'dist_i_cnt_y2', 'dist_i_cnt_y3', 'dist_all_cnt_y3', 'cabin_hi_cnt_y1',
       'cabin_hi_cnt_y2', 'cabin_hi_cnt_y3', 'flt_delay_time_m3',
       'flt_delay_time_m6', 'tkt_3y_amt', 'tkt_avg_amt_y3',
       'tkt_avg_interval_y2', 'tkt_avg_interval_y3', 'pit_all_amt',
       'pit_accu_air_amt', 'pit_now_cons_amt', 'pit_accu_amt_y3',
       'pit_avg_amt_y2', 'pit_avg_amt_y3', 'pit_add_chnl_y2',
       'pit_add_chnl_y3']
X_test=test_data.loc[:, select_features]
# 创建标准化对象
scaler = StandardScaler()
# 对数据进行标准化
X_scaled = scaler.fit_transform(X_test)
# X_scaled=to_csv("test1.csv", index=False)
# 对测试数据进行预测
y_pred = model.predict(X_scaled)
plt.plot(y_pred)
plt.show()
print(y_pred)


