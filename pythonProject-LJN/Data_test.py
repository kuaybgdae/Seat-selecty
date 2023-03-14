import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np

# 加载模型
model = tf.keras.models.load_model('./my_model.h5')

# 读取数据集
test_data = pd.read_csv("test.csv")
# 对数据集进行编码
encoder=LabelEncoder()
for col in test_data.select_dtypes(include='object'):
    test_data[col] = encoder.fit_transform(test_data[col].astype(str))

# 创建示例数据集
features_to_scale=['seg_route_to', 'seg_flight', 'seg_cabin', 'pax_fcny', 'emd_lable',
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
x_test=test_data.loc[:,features_to_scale]
# 对选定的特征进行标准化
scaler = StandardScaler()
X_scaled=scaler.fit_transform(x_test)
# 使用训练好的模型进行预测
y_pred = model.predict(X_scaled)
print(y_pred)
# 将预测值转换为类别标签
y_pred_lables=np.argmax(y_pred, axis=1)
print(y_pred_lables)
