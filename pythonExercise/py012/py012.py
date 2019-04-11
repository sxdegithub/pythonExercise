# coding=utf-8
# https://github.com/Show-Me-the-Code/show-me-the-code

# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，
# 则变成「**是个好城市」。

# 想法(不一定对):
# 1.循环去调用string的replace方法


def filter(file_path):
    with open(file_path, encoding="utf-8") as f:
        words = [word.strip() for word in f]

    while True:
        user_input = input("请输入(提示:CTRL+C可结束): ")
        for word in words:
            length = len(word)
            user_input = user_input.replace(word, "*" * length, -1)

        print("user_input --->{}".format(user_input))


if __name__ == "__main__":
    file_path = "./filtered.txt"
    filter(file_path)
