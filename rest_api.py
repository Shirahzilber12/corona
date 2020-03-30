from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

#  client = MongoClient("mongodb://db:27017")
client = MongoClient("mongodb://localhost:27017/myDatabase")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    'num_of_users': 0
})


class Visit(Resource):
    @staticmethod
    def get():
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"num_of_users": new_num}})
        return str("Hello user " + str(new_num))


def check_posted_data(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            # Missing parameter
            return 301 
        else:
            return 200
    elif function_name == "division":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    @staticmethod
    def post():
        # If I am here, then the resouce Add was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "add")
        if status_code!=200:
            ret_json = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x+y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Subtract(Resource):
    @staticmethod
    def post():
        #  If I am here, then the resouce Subtract was requested using the method POST

        #  Step 1: Get posted data:
        posted_data = request.get_json()

        #  step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "subtract")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        #  If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        #  Step 2: Subtract the posted data
        ret = x-y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Multiply(Resource):
    @staticmethod
    def post():
        #  If I am here, then the resouce Multiply was requested using the method POST

        #  Step 1: Get posted data:
        posted_data = request.get_json()

        #  step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "multiply")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        #  If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        #  Step 2: Multiply the posted data
        ret = x*y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Divide(Resource):
    @staticmethod
    def post():
        #  If I am here, then the resource Divide was requested using the method POST

        #  Step 1: Get posted data:
        posted_data = request.get_json()

        #  step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "division")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(ret_json)

        #  If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        #  Step 2: Multiply the posted data
        ret = (x*1.0)/y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")
api.add_resource(Visit, "/hello")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
