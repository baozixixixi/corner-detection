# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:44:59 2024

@author: Andrey Liao
"""

from ultralytics import YOLO

# Load a model

model = YOLO('./runs/detect/Dandelion/weights/best.pt')  # load a pretrained model (recommended for training)


# Train the model
validation_results = model.val(data='Dandelion.yaml',imgsz=640,batch=16,conf=0.25,iou=0.6,device='0')
