# Bikes-Classification
CNN Image Classifier

Overview

A Simple Deep Neural Network to classify images made with Keras. This supports binary classification.
Mountain Bike and Road Bike Classifier using CNN.

Requirements

Code is written in Python 3.5 and requires:

Keras 2.1.3 (TensorFlow backend)
Skimage 0.13.1
Numpy 1.14.0
OpenCV 3.4.0


Dataset

The images are here (the images are the same, two download options provided for redundancy):
Google Drive:
https://drive.google.com/drive/folders/1ywyfiAEI0ql81gMy58UeamWvV7u9xGn9?usp=sharing
OneDrive:
https://1drv.ms/f/s!AoYpNs_C1pusgxvM3sOU5Wn9yJm5

Usage

First, collect training and test data and deploy it like this for Binary classification:

./data/
  train/
    mountainbike/
      mountain_bike_0.jpg
      mountain_bike_0.jpg
         .......
    roadbike/
      road_bike_0.jpg
      road_bike_1.jpg
        ........
  validation/
    mountainbike/
      mountain_bike_0.jpg
      mountain_bike_0.jpg
         .......
    roadbike/
      road_bike_0.jpg
      road_bike_1.jpg
        ........
    
