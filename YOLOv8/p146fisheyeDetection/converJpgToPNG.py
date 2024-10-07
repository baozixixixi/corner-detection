# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:15:13 2024

@author: Andrey Liao
"""


import cv2
import os
 
# 图片文件夹路径
folder_path = 'F:/dunbaoData/labelData/329/images/'
 
# 检查文件夹路径是否存在
if not os.path.exists(folder_path):
    print("The folder path does not exist.")
    exit()
 
# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 构建完整的文件路径
    file_path = os.path.join(folder_path, filename)
    
    # 检查是否为图片文件
    if file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        # 读取图片
        image = cv2.imread(file_path)
        
        # 如果读取失败，则跳过这个文件
        if image is None:
            print(f"Error: unable to read the file: {file_path}")
            continue
        
        # 转换图片格式为PNG
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_path = os.path.join(folder_path, png_filename)
        cv2.imwrite(png_path, image)
        print(f"Converted: {filename} to {png_filename}")