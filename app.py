from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

# 创建 Flask 应用程序
app = Flask(__name__)

# 加载训练好的神经网络模型
model = tf.keras.models.load_model('my_model.h5')

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ticket')
def ticket():
    return '购买机票页面'

@app.route('/order')
def order():
    return '查看订单页面'

@app.route('/user_passage')
def user_passage():
    return '查看用户信息页面'

@app.route('/predict',methods=['POST','GET'])
def predict():
    # 从 POST 请求中获取数据
    data = request.json
    # 将数据转换为 numpy 数组
    input_data = np.array(data['input'])
    # 使用模型进行预测
    output_data = model.predict(input_data)
    # 将预测结果转换为 JSON 格式并返回
    return jsonify({'output': output_data.tolist()})
# 启动应用程序

if __name__ == '__main__':
    app.run()

