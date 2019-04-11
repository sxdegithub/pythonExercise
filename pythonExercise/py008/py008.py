# coding=utf-8
# 第 0008 题：一个HTML文件，找出里面的正文。

# 使用正则匹配<body >....</body>之间的内容

import re

file_path = r"C:\Users\ssau\PycharmProjects\pythonExercise\py008\news.html"

with open(file_path, encoding="utf-8") as f:
    text = f.read()
    data = re.search("<body(.|\s)*/body>", text)
    print(data.group(0))


