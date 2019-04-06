# coding=utf-8
# **第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 打开存放日记的目录
# 找到里面所有的txt文件
# 循环读文件
# 统计单个文件中单词出现频率
# 将所有文件中单词出现频率合并

import os
import pathlib
import re

diary_path = "C:\\Users\\ssau\\PycharmProjects\\pythonExercise\\py006"
# diary_files = os.listdir(diary_path)

# 过滤出txt文
# 件来
path = pathlib.Path(diary_path)
diary_files = path.glob("*.txt")

mapping = dict()
for i in diary_files:
    # print(i)
    print(os.path.split(i)[-1])
    with open(i, encoding="utf-8") as f:
        data = f.read()
        # 匹配所有word
        words = re.findall("\w+", data)
        words = [word.lower() for word in words]
        # 将word数量存入字典
        for word in words:
            mapping[word] = mapping.get(word, 0) + 1
        # print(mapping)
        # print(word)
# 对字典排序
# python内置的Counter可以实现,未尝试过
mapping = sorted(mapping.items(), key=lambda item: item[-1], reverse=True)
print(mapping[:5])
