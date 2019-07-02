from flask import Flask

import email_util

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_email')
def send_email():
    email_util.send()
    return 'Mail Sent!'


if __name__ == '__main__':
    app.run()
