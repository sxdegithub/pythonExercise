# coding=utf-8
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。/
# https://github.com/Show-Me-the-Code/show-me-the-code

"""
想法(不一定对):
1.把敏感词读入到list里面
2.用户输入的时候，将输入和list对比
3.如果输入词在字典里面，则打印Freedom，否则打印HumanRights
"""


def filter_word(filter_file_path):
    # 读取需要过滤的关键词
    with open(filter_file_path, encoding="utf-8", mode="r") as f:
        filter_words = [word.strip() for word in f]
    # print("filterWords -->{}".format(filterWords))
    while True:
        user_input = input("请输入(提示： 输入CTRL + C ，退出):    \n")
        if user_input in filter_words:
            print("Freedom")
        else:
            print("Human Rights")


if __name__ == "__main__":
    filterFilePath = "./filtered.txt"
    filter_word(filterFilePath)
