# coding=utf-8
# https://github.com/Yixiaohan/show-me-the-code
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont

pic_path = r"C:\Users\ssau\Documents\python-show-me-code\000\headPic.jpg"
# 获取图片对象
im = Image.open(pic_path)
# 获取图片宽高
w, h = im.size

print(w, h)

# 获取绘图对象
draw = ImageDraw.Draw(im)

# 字体对象
font = ImageFont.truetype(font=r"C:\Users\ssau\Documents\python-show-me-code\000\arial.ttf", size=55)       
# 颜色对象
fillcolor = "#ff0000"
# 在图片上面绘制数字
draw.text((650, 50), "99", fill=fillcolor, font=font)
im.save(r"C:\Users\ssau\Documents\python-show-me-code\000\headPic2.jpeg")


