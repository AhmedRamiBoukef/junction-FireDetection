import cv2 as cv
from app import yolo 
from PIL import Image
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) 
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame)
    detections = yolo(pil_image)
    if not detections.empty:
        print("Fire detected")
        data = 1
        ser.write(data.encode())
    else : 
        data = 0
        ser.write(data.encode())
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

ser.close()
capture.release()
cv.destroyAllWindows()