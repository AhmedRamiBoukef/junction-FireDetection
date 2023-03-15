
# BlazeBlocker

Our deep learning model is based on YOLO, a state-of-the-art object detection algorithm that is widely used for a range of computer vision tasks. In our case, we have fine-tuned the YOLO model specifically for fire detection, enabling it to identify fires with a high degree of accuracy.

The model is capable of analyzing video feeds from a camera and detecting any instances of fire. When a fire is detected, the model draws a bounding box around the fire in the video feed, allowing the user to quickly identify the location of the fire.

In addition to detecting fires, the model is also capable of sending signals to an Arduino board. Specifically, when a fire is detected, the model sends a signal of 1 to the Arduino, indicating that action needs to be taken to suppress the fire. If no fire is detected, the signal sent is 0, indicating that there is no need for action.

We have fine-tuned the model using a large dataset of images and videos of fires in various environments and lighting conditions. By carefully labeling the data and training the model on it, we have achieved an accuracy of over 95%, meaning that the model is highly effective at detecting fires.


For more details : https://drive.google.com/file/d/1lVEwTyi3qJjpKUl9FuOVZMwXotjzE7Gn/view?usp=sharing

## Screenshots


![Capture d'écran 2023-03-11 175154](https://user-images.githubusercontent.com/77940258/224508849-d16f7ec9-f77b-41db-b8a2-899e84b006dc.png)

## Links

link to Simulation : https://www.tinkercad.com/things/dQlWQdoAZTe-fantastic-jaban-migelo/editel?sharecode=ca4KtSN82vZNZ5OGM4QLJVcmGCNCfirHzD1sQWo8N3M

link to video : https://drive.google.com/file/d/1lVEwTyi3qJjpKUl9FuOVZMwXotjzE7Gn/view?usp=sharing

## Feedback

If you have any feedback, please reach out to us at ka_boukef@esi.dz

