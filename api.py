from flask import Flask, render_template
import socketio

# Create a Socket.IO server
sio = socketio.Server(async_mode='threading')
app = Flask(__name__)

# Attach the Socket.IO server to the Flask app
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@app.route('/')
def index():
    return render_template('index.html')

@sio.event
def connect(sid, environ):
    print(f'Client {sid} connected')
    sio.emit('message', {'msg': 'Welcome!'}, to=sid)

@sio.event
def disconnect(sid):
    print(f'Client {sid} disconnected')

@sio.event
def message(sid, data):
    print(f'Received message: {data}')
    sio.emit('message', {'msg': data['msg']}, skip_sid=sid)

if __name__ == '__main__':
    app.run(debug=True)
