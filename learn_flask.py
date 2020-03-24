from flask import Flask, jsonify, request

app = Flask(__name__)


# http://127.0.0.1:5000
@app.route('/')
def hello_world():
    return "hello world"


@app.route('/hi_there')
def hi_there():
    # c = 1/0
    age = 4
    ajson = {
        'Age': age,
        'b': '456'
    }
    return jsonify(ajson)


@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # get to num from postman data
    data_dict = request.get_json()
    x = data_dict['x']
    y = data_dict['y']
    z = x+y
    ajson = {
        'sum': z,

    }
    return jsonify(ajson), 200


if __name__ == '__main__':
    app.run()
