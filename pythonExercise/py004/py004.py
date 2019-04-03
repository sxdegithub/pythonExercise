# coding=utf-8
# https://github.com/Show-Me-the-Code/show-me-the-code
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

# 打开文件
# 利用正则去匹配
# 把结果存到字典里面去

import re

file_path = r"./log.txt"
with open(file_path, encoding="utf-8") as f:
    text = f.read()
    # print(words)
    words = re.findall("\w+", text)
    print("words type is {}".format(type(words)))
    print("words length is {}".format(len(words)))
    # print(words)
    # 单词全部小写
    words = [w.lower() for w in words]
    mapping = dict()
    # 将单词数量作为键值存入到字典里.
    for word in words:
        mapping[word] = mapping.get(word, 0) + 1
    print("mapping is : {}".format(mapping))
    print("mapping.items():{}".format(mapping.items()))

    # 按着单词出现的次数高低排序.
    sorted_result = sorted(mapping.items(), key=lambda item: item[1], reverse=True)
    for i in sorted_result:
        print(i)
