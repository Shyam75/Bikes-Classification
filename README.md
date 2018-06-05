# Bikes-Classification

CNN Image-Binary Classifier

Overview
A Simple Deep Neural Network to classify images made with Keras. This supports binary classification for images of mountain and road bikes.

Requirements
Keras = 2.x (TensorFlow backend)
Numpy = 1.x
OpenCV 3.4

Datset
The images are here (the images are the same, two download options provided for redundancy):
Google Drive:
https://drive.google.com/drive/folders/1ywyfiAEI0ql81gMy58UeamWvV7u9xGn9?usp=sharing
OneDrive:
https://1drv.ms/f/s!AoYpNs_C1pusgxvM3sOU5Wn9yJm5


Usage
First, collect training and validation data and deploy it like this for binary classification.

./data/
  train/
    mountainbike/
      mountain_bike_0.jpg
      mountain_bike_1.jpg
        ...........
    roadbike/
      road_bike_0.jpg
      road_bike_1.jpg
        ...........
  
  
  validation/
    mountainbike/
      mountain_bike_0.jpg
      mountain_bike_1.jpg
        ...........
    roadbike/
      road_bike_0.jpg
      road_bike_1.jpg
        ...........
      
