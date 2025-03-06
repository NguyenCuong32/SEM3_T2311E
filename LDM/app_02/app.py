from flask import Flask, jsonify
from app_02.data_util import data

app = Flask(__name__)
@app.route('/api/v1/message',methods = ['GET'])


def get_data():
    return data.get_database()
    # return jsonify({"message":"Hello"})

if __name__ == "__main__":
    app.run(debug = True)