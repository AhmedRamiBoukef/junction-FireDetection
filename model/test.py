import cv2 as cv
from app import yolo 
from PIL import Image


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    detections = yolo(pil_image)
    if not detections.empty:
        print("Fire detected")
        for _, detection in detections.iterrows():
            x1, y1 = int(detection['xmin']), int(detection['ymin'])
            x2, y2 = int(detection['xmax']), int(detection['ymax'])
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()