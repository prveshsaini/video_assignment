# Real-Time Object Detection Video Streaming App

This project is a Flask-based web application that streams live video from a webcam (or IP camera) and performs real-time object detection using YOLOv8 from Ultralytics

## Project Structure

```
video_streaming/
│
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # Frontend HTML page
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Features

- Real-time video streaming in browser
- Object detection using YOLOv8 (lightweight yolov8n.pt model)
- Works with webcam or IP camera stream
- Flask-based lightweight web server

## Requirements

Python 3.8 or higher

A working webcam (or an IP camera stream URL)

Internet connection (for downloading YOLO model weights the first time)

## Installation

Clone the repository

git clone https://github.com/prveshsaini/video_assignment.git
cd video_streaming


Create and activate a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


Install dependencies

pip install -r requirements.txt


Example requirements.txt might include:

Flask
opencv-python
ultralytics

## Running the App

Start the Flask server

python app.py


Open your browser and navigate to:

http://127.0.0.1:5000


You should see a live video feed with detected objects highlighted in real time.


## How It Works

Flask serves a simple HTML page (index.html) with an embedded video stream.

The /video_feed route continuously generates frames using OpenCV.

Each frame is processed by the YOLOv8 model for object detection.

Detected results are drawn on the frame using results[0].plot().

Frames are encoded as JPEG and streamed as a multipart response to the browser.