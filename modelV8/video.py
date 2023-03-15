from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import imutils
import cv2

model = YOLO("best.pt")
model.overrides['conf'] = 0.3
model.overrides['iou'] = 0.45
capture = cv2.VideoCapture(0)

fov = 320

while True:
    isTrue, frame = capture.read()
    if not isTrue :
        break
    results = model.predict(source=frame)
    res_plotted = results[0].plot()
    classes = results[0].boxes.cls
    detections = results[0].boxes.boxes.numpy()
    names = [model.names[int(cls)] for cls in classes]
    if names:
        max = 0
        square = (detections[0][2] - detections[0][0]) * (detections[0][3] - detections[0][1])
        maxlist = detections[0]
        for i in range(len(detections)):
            if (detections[i][2] - detections[i][0]) * (detections[i][3] - detections[i][1]) > square:
                square = (detections[i][2] - detections[i][0]) * (detections[i][3] - detections[i][1])
                max = i
                maxlist = detections[i]
        h, w = image.shape[:2]
        cx = maxlist[0]
        cy = maxlist[1]
        angle_x = math.atan((cx - w / 2) * math.tan(math.radians(fov) / 2) / (w / 2))
        angle_y = math.atan((cy - h / 2) * math.tan(math.radians(fov) / 2) / (h / 2))
        cx2 = maxlist[0]
        cy2 = maxlist[1]
        angle_x2 = math.atan((cx2 - w / 2) * math.tan(math.radians(fov) / 2) / (w / 2))
        angle_y2 = math.atan((cy2 - h / 2) * math.tan(math.radians(fov) / 2) / (h / 2))
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