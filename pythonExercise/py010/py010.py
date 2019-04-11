# coding=utf-8
# 第 0010 题：使用 Python 生成类似于下图中(example.jpg)的字母验证码图片

# 参考:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000

# 想法(不一定对):
# 使用PIL打开一个画布(or 打开一个空白图片)
# 生成四个随机字符
# 将字符写入到图片上
# 对图片进行模糊处理

import random
import string

from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 生成验证码
def get_code():
    letters = string.ascii_letters
    digit = string.digits
    population = letters + digit
    # print("population --->{}".format(population))
    # 使用random生成四个随机字符.
    ver_code = "".join(random.sample(population, 4))
    # print("ver_code -->{}".format(ver_code))
    return ver_code


# 生成一个随机字符
# def randchr():
#     return chr(random.randint(65, 90))

# 生成背景随机颜色
def rand_color():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))


# 生成字符的随机颜色
def rand_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


size = (240, 60)
img = Image.new("RGB", size=size, color=(255, 255, 255))
fnt = ImageFont.truetype(font=r"C:\Windows\Fonts\arial.ttf", size=50)
draw = ImageDraw.Draw(img)
fillcolor = "#ff0000"

# 对背景做随机颜色填充
for i in range(0, 240):
    for j in range(0, 60):
        draw.point((i, j), rand_color())

code = get_code()
print("code --->{}".format(code))

# 在图片上绘制验证码的字符
for i in code:
    draw.text((40 + 40 * code.index(i), 5), i, fill=rand_color2(), font=fnt)

#  将字符写入到图片上
# draw.text((60, 5), ver_code, fill=fillcolor, font=fnt)

# 模糊处理
img = img.filter(ImageFilter.BLUR)

img.save("blank_a.png", "png")
# img.show()
