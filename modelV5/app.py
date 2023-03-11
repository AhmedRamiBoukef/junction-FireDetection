from PIL import Image
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')


def yolo(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS) 
    results = model(im) 
    results.render()
    detections = results.pandas().xyxy[0]

    return detections

# img = yolo(Image.open("image.jpg"))
# img.show()
