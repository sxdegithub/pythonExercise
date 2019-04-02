# coding=utf-8

# https://github.com/Yixiaohan/show-me-the-code
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

# 封装下添加数字的方法
from PIL import Image, ImageDraw, ImageFont


def add_num(img_path, num):
    # image object
    img = Image.open(img_path)
    w, h = img.size
    print(w, h)
    print("num:", num)
    # font
    fnt = ImageFont.truetype("arial.ttf", size=100)
    # draw object
    draw = ImageDraw.Draw(img)
    # color
    fillcolor = (255, 255, 255, 128)
    # draw num on picture
    draw.text((w * 0.7, h * 0.05), str(num), fill=fillcolor, font=fnt)
    img.save(picPath.split(".")[0] + "2.jpeg")


if __name__ == "__main__":
    picPath = r"headPic.jpg"
    num = 100
    add_num(picPath, num)
