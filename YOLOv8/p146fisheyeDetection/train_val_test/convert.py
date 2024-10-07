# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:44:59 2024

@author: Andrey Liao
"""

from ultralytics import YOLO

# Load a model
from ultralytics import YOLO
# Load a model
model = YOLO('best.pt')  # load an official model
# Export the model
model.export(format='onnx', dynamic=False,imgsz=[640,640], opset=12)

