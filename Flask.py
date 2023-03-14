from flask import Flask, request, jsonify
from my_pycharm_program import my_function

app = Flask(__name__)

@app.route('/my-api-endpoint', methods=['GET'])
def hello_world():
    return 'Hello, World!'
def my_api_endpoint():
    data = request.get_json()
    result = my_function(data)
    return jsonify(result)
if __name__ == '__main__':
    app.run()
