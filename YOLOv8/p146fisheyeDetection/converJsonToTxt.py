# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:17:49 2024

@author: Andrey Liao
"""

import json
import os
 
 
def convert_annotation(json_file, txt_file, label_to_id_mapping):
    # Read the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
 
        # Extract image dimensions, assuming 'imageWidth' and 'imageHeight' fields are present
    image_width = data.get('imageWidth')
    image_height = data.get('imageHeight')
 
    # Check if image dimensions are present
    if image_width is None or image_height is None:
        raise ValueError(f"Missing image dimensions in {json_file}")
 
        # Iterate over all shapes (annotations)
    with open(txt_file, 'w', encoding='utf-8') as out_file:
        for shape in data.get('shapes', []):
            # Extract point coordinates, assuming each shape has a 'points' field
            points = shape.get('points', [])
 
            # Check if points are present
            if not points:
                raise ValueError(f"Missing points in a shape in {json_file}")
 
            x_values = [point[0] for point in points]
            y_values = [point[1] for point in points]
 
            x_min = min(x_values)
            y_min = min(y_values)
            x_max = max(x_values)
            y_max = max(y_values)
 
            # Calculate bounding box center, width, and height
            bbox_center_x = (x_min + x_max) / 2
            bbox_center_y = (y_min + y_max) / 2
            bbox_width = x_max - x_min
            bbox_height = y_max - y_min
 
            # Convert bounding box coordinates to ratios relative to image dimensions
            bbox_center_x_ratio = bbox_center_x / image_width
            bbox_center_y_ratio = bbox_center_y / image_height
            bbox_width_ratio = bbox_width / image_width
            bbox_height_ratio = bbox_height / image_height
 
            # Get the category ID, assuming each shape has a 'label' field
            category_id = shape.get('label', "unknown")
            if isinstance(category_id, str):
                # If the label is a string, map it to a numeric ID using the provided mapping
                category_id = label_to_id_mapping.get(category_id, -1)  # Default to -1 if label is unknown
 
            # Write the result to the TXT file in YOLO format
            out_file.write(
                f"{int(category_id)} {bbox_center_x_ratio} {bbox_center_y_ratio} {bbox_width_ratio} {bbox_height_ratio}\n")
 
        # Input and output folder paths
 
 
input_folder = 'E:/AVM_Project/BS/dlCorners/json'
output_folder = 'E:/AVM_Project/BS/dlCorners/txt'
os.makedirs(output_folder, exist_ok=True)
 
# 标注物体的类别名
label_to_id_mapping = {
    'corner': 0
    # Add more mappings as needed
}
 
# Iterate over all JSON files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        json_file = os.path.join(input_folder, filename)
        txt_file = os.path.join(output_folder, filename.replace('.json', '.txt'))
        try:
            convert_annotation(json_file, txt_file, label_to_id_mapping)
            print(f'{txt_file},Conversion successful!')
        except Exception as e:
            print(f"An error occurred while processing {json_file}: {e}")