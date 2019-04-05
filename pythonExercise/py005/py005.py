# coding=utf-8
# # https://github.com/Show-Me-the-Code/show-me-the-code
# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

# 他人解法 http://www.cnblogs.com/RChen/archive/2007/03/31/pil_thumb.html

# 想法:
# 打开这个目录
# 遍历这个目录的文件,过滤掉非图片文件
# 按比例循环改变图片的分辨率,保证长或者宽不大于6s的分辨率

import os
import sys
from PIL import Image, ImageDraw, ImageFont

file_path = "C:\\Users\\ssau\\Pictures\\"

files = os.listdir(file_path)

# 图片格式
pic_postfix = ("jpeg", "png", "png", "gif", "jpg")

print("list of files :{}".format(files))

pics = []
# 判断文件后缀是否是图片格式
for i in files:
    if i.split(".")[-1].lower().strip() not in pic_postfix:
        print("i.split('.')[-1].lower()  -->", i.split(".")[1].lower().strip())
        files.remove(i)

# 图片文件列表
print(" pictures :{} ".format(files))
for i in files:
    print("file paths -->{}<--".format(file_path + i))

for i in files:
    img = Image.open(file_path + i)
    width, height = img.size
    if width >= 750 or height >= 1334:
        # 确定缩小比例
        value = max(height / 1334, width / 750)
        scale_size = (int(width / value), int(height / value))
        out = img.resize(scale_size, Image.ANTIALIAS)
        # # 疑问:部分生成的图片会逆时针旋转90°
        out.save((file_path + i).split(".")[0] + "_new.jpeg", "jpeg")
