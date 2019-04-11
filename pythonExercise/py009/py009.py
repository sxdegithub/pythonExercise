# coding=utf-8
# 第 0009 题：一个HTML文件，找出里面的链接。

import re

file_path = r"C:\Users\ssau\PycharmProjects\pythonExercise\py008\news.html"

# 正则匹配所有链接

with open(file_path, encoding="utf-8", mode="r") as f:
    text = f.read()
    # (?=exp)前向搜索肯定模式,(?!exp)前向搜索否定模式
    # (?<=exp)后向搜索肯定模式,(?<!exp)后向搜索否定模式
    # 这里用了一个前向搜索肯定模式,用来去除结尾处的双引号 " 符号
    url = 'https?://[^\\s]*(?=")'
    # 预编译匹配模式,re.I忽略大小写
    pattern = re.compile(url, re.I)
    data = re.findall(pattern, text)
    for url in data:
        print("url -->{}".format(url))
