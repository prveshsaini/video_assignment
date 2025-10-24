from flask import Flask, render_template, Response
import cv2
from threading import Lock

from ultralytics import YOLO

app = Flask(__name__)

# Initialize video capture (0 = webcam, or replace with IP camera URL)
# Example: "rtsp://username:password@192.168.0.5:554/stream"
camera = cv2.VideoCapture(0)
lock = Lock()

model = YOLO("yolov8n.pt")

def generate_frames():
    """Generator that yields camera frames encoded as JPEG."""
    while True:
        with lock:
            success, frame = camera.read()
            if not success:
                break

            results = model(frame, verbose=False)
            frame = results[0].plot()

            # Encode frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

        # Stream as multipart JPEG
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    """Home page with live video feed."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
