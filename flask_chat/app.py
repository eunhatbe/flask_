import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("connect")
def connect():
    print("connect")

@socketio.on("message")
def request(message):
    print("message: " + message)
    to_client = dict()

    if message == "new_connect":
        to_client["message"] = "welcome tester"
        to_client["type"] = "connect"
    else:
        to_client["message"] = message
        to_client["type"] = "normal"

    send(to_client, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
