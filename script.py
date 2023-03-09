import cv2 as cv
from app import yolo 
from PIL import Image


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame)
    detections = yolo(pil_image)
    if not detections.empty:
        print("No objects detected in the image.")
    # img.show()
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()