# coding=utf-8
# **第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# 匹配空行
# 匹配注释,首字符为#,暂时不匹配代码块
# 匹配代码行

# 统计example.py中数据
file_path = r"C:\Users\ssau\PycharmProjects\pythonExercise\py007\example.py"
# 使用字典存储数据
sum_lines = {"code": 0, "comment": 0, "space": 0}
# 逐行阅读,去掉行的空格
with open(file_path, mode="r", encoding="utf-8") as f:
    # 一下全部读,耗费内存会多,逐行读可以节约内存

    # <--------节约内存,逐行读取
    # line = f.readline()
    # while line:
    #     print("line ---->{}".format(line), end="")
    #     line = f.readline()
    # 节约内存,逐行读取-------->

    lines = f.readlines()
    # lines = [line.strip() for line in lines]
    for line in lines:
        # 检测空行,code行 ,#开头的注释行,暂时未实现"""代码块"""的分辨
        if line.strip() == "":
            sum_lines["space"] = sum_lines.get("space", 0) + 1
        elif line.strip()[0] == "#":
            sum_lines["comment"] = sum_lines.get("comment", 0) + 1
        else:
            sum_lines["code"] = sum_lines.get("code", 0) + 1
print("sum_lines -->{}".format(sum_lines))
