import torch
import cv2
import datetime
from ultralytics import YOLO
import numpy as np
from PIL import Image

print(torch.cuda.is_available())  # Returns True if GPU is available
print(torch.cuda.device_count())  # Number of GPUs available
# print(torch.cuda.get_device_name(0))  # Name of the first GPU

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
import os
HOME = os.getcwd()
print(HOME)

# Load the YOLOv11 model
# model = torch.hub.load('ultralytics/yolov11', 'custom', path='yolo11n.pt')
# model = YOLO("trash2_model.pt")
model = YOLO("trash2_model.pt")


# Define configuration constants
CONFIDENCE_THRESHOLD_LIMIT = 0.5
BOX_COLOUR = (0, 255, 0)

# Define the device type. Set to "mps" if you want to use M1 Mac GPU. Otherwise use "cpu"
DEVICE = "0"

# Define video source. You can use a webcam, video file ir a live stream
VIDEO_SOURCE = cv2.VideoCapture(0)  # 0 for webcam
# VIDEO_SOURCE = cv2.VideoCapture('data/video.mp4')

# Perform object detection on an image
# results = model("trash3.png")
# image_path = "trash5.png"
# image = Image.open(image_path)
# resized_image = image.resize((640, 640))
# results = model(resized_image)
# results[0].show()

# Export the model to ONNX format
# path = model.export(format="onnx")  # return path to exported model



while True:
    start = datetime.datetime.now()
    ret, frame = VIDEO_SOURCE.read()

    # if there are no more frames to process, stop the loop
    if not ret:
        break

    # Perform object detection. Set MPS is the device type
    detections = model(frame, device=DEVICE)
    result = model(frame)[0]

    # Transform the results to numpy arrays and integers. Pixels are always integers
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(result.boxes.cls.cpu(), dtype="int")
    confidence = np.array(result.boxes.conf.cpu(), dtype="float")

    # Draw the bounding boxes and labels on the frame. The color of the bounding box depends on the confidence
    for cls, bbox, conf in zip(classes, bboxes, confidence):
        (x, y, x2, y2) = bbox
        object_name = model.names[cls]
        if conf < CONFIDENCE_THRESHOLD_LIMIT:
            continue
        if conf > 0.6:
            BOX_COLOUR = (37, 245, 75)
        elif conf < 0.6 and conf > 0.3:
            BOX_COLOUR = (66, 224, 245)
        else:
            BOX_COLOUR = (78, 66, 245)

        cv2.rectangle(frame, (x, y), (x2, y2), BOX_COLOUR, 2)
        cv2.putText(frame, f"{object_name}: {conf:.2f}", (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 2, BOX_COLOUR, 2)

    # Measure time it took to process 1 frame and overlay fps on the frame
    end = datetime.datetime.now()
    total = (end - start).total_seconds()

    # Calculate the frame per second and draw it on the frame
    fps = f"FPS: {1 / total:.2f}"
    cv2.putText(frame, fps, (50, 50),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    # Display the output video
    cv2.imshow("Output video", frame)

    # Stop processing when the "q" key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

VIDEO_SOURCE.release()
cv2.destroyAllWindows()
