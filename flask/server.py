import socketio
from flask import Flask
import cv2
import os,shutil

# function to capture frames using opencv
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = True

    while success: 
        success, image = vidObj.read() 
        if image is not None:
            cv2.imwrite(f"./public/frame{count}.jpg", image) 
            count += 1


app = Flask(__name__)
@app.get('/')
def home():
    return "hi"

# Create a new Socket.IO client
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print('Connected to Node.js server')
@sio.event
def disconnect():
    print('Disconnected from Node.js server')

@sio.event
def process_video(data):
    FrameCapture('../public/temp/'+data)
    sio.emit('data','result from ml model')
    shutil.rmtree('./public')
    os.mkdir('./public')

# Connect to the Node.js server
sio.connect('http://localhost:8000')

# Optionally emit messages to the Node.js server
sio.emit('message_from_flask', {'data': 'Hello from Flask!'})
# Run the Flask app
if __name__ == '__main__':
    socketio.run(app, port=5000)
