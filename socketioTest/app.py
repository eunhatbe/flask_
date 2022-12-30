from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testkey'
Socketio = SocketIO(app)

@app.route('/')
def seesions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received...')

@Socketio.on('my_event')
def handle_my_custom_event(json, methods=['GET','POST']):
    print('received my event: ' + str(json))
    Socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    Socketio.run(app, debug=True)

