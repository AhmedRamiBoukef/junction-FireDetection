from PIL import Image
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')  # force_reload=True to update


def yolo(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize
    results = model(im)  # inference
    results.render()  # updates results.ims with boxes and labels
    detections = results.pandas().xyxy[0]  # get detections

    return detections

# img = yolo(Image.open("image.jpg"))
# img.show()
