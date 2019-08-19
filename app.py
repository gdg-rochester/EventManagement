import json

from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import devfest_util
import email_util

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.data
    data = json.loads(data)
    # print(data)
    email_util.send(data)
    return 'Mail Sent!'


@app.route('/get_attendees', methods=['GET'])
def get_attendees():
    return jsonify(devfest_util.get_attendees())


@app.route('/get_attendees_2', methods=['GET'])
def get_attendees_2():
    return jsonify(devfest_util.get_attendees_2())


if __name__ == '__main__':
    app.run()
