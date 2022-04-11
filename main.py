import cv2
import datetime
from controllers.store import createData
from cv2 import threshold
from numpy import size

# Load Model
net = cv2.dnn.readNet("yolov4\yolov4-tiny.weights", "yolov4\yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# Load classes
classes = []
with open("yolov4\classes.txt", "r") as file:
    for class_name in file:
        classes.append(class_name.strip())

# Initialize Camera
cap = cv2.VideoCapture(0)



while True:
    # Get Frame
    ret, frame = cap.read()

    # Object detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        rounded_score = str(round(score, 2))
        threshold = 0.7
        createData(class_name, str(datetime.datetime.now()))

        if score > threshold:
            if class_id == 0:
                cv2.putText(frame, str(class_name + ' ({})'.format(rounded_score)), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 40), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 40), 3)
            else:
                cv2.putText(frame, str(class_name + ' ({})'.format(rounded_score)), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 200), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)