import socketio
from flask import Flask
import cv2
import os,shutil
# import torch
# import pickle 
# import model
# from model import linearRegression
# test_model = pickle.load(open('linear_regression1.sav', 'rb') )
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    # Used as counter variable 
    count = 0
    # checks whether frames were extracted 
    success = 1
    while success: 
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        # Saves the frames with frame-count 
        
        cv2.imwrite("./public/frame%d.jpg" % count, image) 
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
    print('Debug debug')
    # print('../public/temp/'+data)
    sio.emit('data','result from ml model')
    shutil.rmtree('./public')
    return "Processed"

# @sio.event
# def parameter(data):
#     test_model.eval()
#     with torch.inference_mode():
#         input_data = torch.tensor(data)
#         preds = test_model(input_data)

#     sio.emit('data',{'data': preds.numpy()})

# Connect to the Node.js server
sio.connect('http://localhost:8000')
# Optionally emit messages to the Node.js server
sio.emit('message_from_flask', {'data': 'Hello from Flask!'})
# Run the Flask app
if __name__ == '__main__':
    socketio.run(app, port=5000)
