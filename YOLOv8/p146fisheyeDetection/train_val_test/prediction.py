# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:44:59 2024

@author: Andrey Liao
"""

from ultralytics import YOLO

# Load a model
model = YOLO('./runs/detect/dunbaocenter/weights/best.pt')  # pretrained YOLOv8n model

# Define path to directory containing images and videos for inference
source = '/home/ubuntu/dataset/detect/dunbaoCenterTrainAndTestData/center/images/test'

# Run batched inference on a list of images
#results = model(['20210519153450.png'])  # return a list of Results objects

# Run inference on 'bus.jpg' with arguments
model.predict(source, save=True, conf=0.25)

# Process results list
#for result in results:
#    boxes = result.boxes  # Boxes object for bounding box outputs
#   masks = result.masks  # Masks object for segmentation masks outputs
#    keypoints = result.keypoints  # Keypoints object for pose outputs
#    probs = result.probs  # Probs object for classification outputs
#    result.show()  # display to screen
#    result.save(filename='result.jpg')  # save to disk
