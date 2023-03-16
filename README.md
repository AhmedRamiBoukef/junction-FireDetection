
# BlazeBlocker

Our solution consists of an AI model that is trained to detect fires using visual images from a fixed camera. The camera has a fixed angle of 320 degrees and captures images of the environment at regular intervals. The AI model analyses these images in real-time to detect any signs of a fire.

When the AI model detects a fire, it sends a signal to the Arduino board with the coordinates of the location of the fire. The Arduino board then uses this information to control two servos, one for dimX and one for dimY, to move the camera towards the exact location of the fire.

Once the camera is in position, the system activates a water pump to extinguish the fire. The water pump is controlled by the Arduino board and can be turned on and off as required. The system also has a safety feature where the water pump turns off automatically once the fire has been extinguished by receiving a 0 value from the AI model.

In case multiple fires are detected simultaneously, an algorithm is implemented to prioritize the fires based on their size, location, and potential impact. The system selects the largest and most dangerous fire as the top priority and moves the camera and water pump to that location first. Once that fire is extinguished, the system moves on to the next fire in order of priority until all fires are extinguished.



For more details : https://drive.google.com/file/d/1lVEwTyi3qJjpKUl9FuOVZMwXotjzE7Gn/view?usp=sharing

## Screenshots


![Capture d'écran 2023-03-11 175154](https://user-images.githubusercontent.com/77940258/224508849-d16f7ec9-f77b-41db-b8a2-899e84b006dc.png)

## Links

link to Simulation : https://www.tinkercad.com/things/kGe8MnTZSjy-copy-of-copy-of-copy-of-fire-detection/editel?sharecode=ZnXVzWs_rE0CLgZ_GlaIsGjsvM1T95OPgz6LiOfc4aw

link to video : https://drive.google.com/file/d/1lVEwTyi3qJjpKUl9FuOVZMwXotjzE7Gn/view?usp=sharing

## Feedback

If you have any feedback, please reach out to us at ka_boukef@esi.dz

