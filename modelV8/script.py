from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import imutils
import cv2
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) 
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

        data = 1
        ser.write(data.encode())
    else :
        print("return 0")
        data = 0
        ser.write(data.encode())
    frame = imutils.resize(res_plotted, width=640)
    cv2.imshow("result", frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

ser.close()
capture.release()
cv2.destroyAllWindows()