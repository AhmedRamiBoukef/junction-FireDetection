from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import imutils

import cv2

model = YOLO("best.pt")

results = model.predict(source="image.jpg")
res_plotted = results[0].plot()
frame = imutils.resize(res_plotted, width=640)
cv2.imshow("result", frame)
cv2.waitKey(0) 
cv2.destroyAllWindows() 