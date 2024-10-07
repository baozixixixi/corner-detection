# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:44:59 2024

@author: Andrey Liao
"""

from ultralytics import YOLO


import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"




# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='fisheyeBBX.yaml', epochs=100, imgsz=640,batch=16,save=True,device='0',name="fisheyebbx",pretrained=True,workers=0)
