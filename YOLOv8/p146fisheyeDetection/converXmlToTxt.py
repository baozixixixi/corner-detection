# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:01:36 2024

@author: Andrey Liao


VOC xml格式转yolo txt格式
"""



import os
import xml.etree.ElementTree as ET

# VOC数据集路径
voc_xml_path = r"E:\AVM_Project\BS\dlCorners\dataAug\xml"
voc_img_path = r"E:\AVM_Project\BS\dlCorners\dataAug\images"
# YOLO数据集路径
yolo_out_txt_path = r"E:\AVM_Project\BS\dlCorners\dataAug\txt"
# VOC类别名称和对应的编号
#classes = {"corner": 0, "green": 1}  # 根据实际情况修改
classes = {"corner": 0}  # 根据实际情况修改

# 遍历VOC数据集文件夹
for filename in os.listdir(voc_xml_path):
    # 解析XML文件
    tree = ET.parse(os.path.join(voc_xml_path, filename))
    root = tree.getroot()
    # 获取图片尺寸
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    # 创建YOLO标注文件
    yolo_filename = filename.replace(".xml", ".txt")
    yolo_file = open(os.path.join(yolo_out_txt_path, yolo_filename), "w")
    # 遍历XML文件中的所有目标
    for obj in root.findall("object"):
        # 获取目标类别名称和边界框坐标
        name = obj.find("name").text
        xmin = int(obj.find("bndbox").find("xmin").text)
        ymin = int(obj.find("bndbox").find("ymin").text)
        xmax = int(obj.find("bndbox").find("xmax").text)
        ymax = int(obj.find("bndbox").find("ymax").text)
        # 计算边界框中心点坐标和宽高
        x = (xmin + xmax) / 2 / width
        y = (ymin + ymax) / 2 / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height
        # 将目标写入YOLO标注文件
        class_id = classes[name]
        yolo_file.write(f"{class_id} {x} {y} {w} {h}\n")
    yolo_file.close()

