from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import imutils
import cv2

model = YOLO("best.pt")
model.overrides['conf'] = 0.3
model.overrides['iou'] = 0.45
capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    if not isTrue :
        break
    results = model.predict(source=frame)
    res_plotted = results[0].plot()
    classes = results[0].boxes.cls
    names = [model.names[int(cls)] for cls in classes]
    if names:
        print("Fire detected")
        print("return 1")
    else :
        print("return 0")
    frame = imutils.resize(res_plotted, width=640)
    cv2.imshow("result", frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()