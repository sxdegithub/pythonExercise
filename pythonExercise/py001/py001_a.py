# coding=utf-8
# https://github.com/Show-Me-the-Code/show-me-the-code
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string

# 大小写字母,数字
letter = string.ascii_letters
digit = string.digits
# 连接后作为取样的population
chars = letter + digit


# print(chars)

# tuple_a = ("222", "112", "3", "224", "22")
# random.sample()
# 生成8个随机字符
def get_8():
    return "".join(random.sample(chars, 8))


# print(" ".join(random.sample(tuple_a, 2)))
# 将4个8位字符通过-拼接
def get_32():
    return "-".join([get_8() for i in range(4)])


# 需要获取的组数
def get_group(num):
    return [get_32() for i in range(num)]


# if __name__ == "__main__":
#     group = get_group(10)
#     for i in group:
#         print(i)

"""
HfLdnuOQ-KS4AhnQH-1KP3RuUG-KLIShGZ3
PYr5WRi2-AsoT9H7f-y4oVxirP-8SiQtw29
KmN16Ysg-lceCaiHJ-y8zDCALo-Nc4iUXvB
Y84Wqctx-mZrR0w3t-vNJj1plb-MlLnxkV5
r1HSyBcP-gSbKBuVj-QutBkVHW-iLBJOgER
7jDgyFSo-m7qazn09-Vfv4Y9rA-yGKFEfUw
dcfF2KMb-U1MJ7cle-Sw05G2fm-XnlzUQDF
wCo27jIp-KPqU0evE-sepUmIyb-TBQps5Vm
cB395Vg7-mI1sOY26-IRu4fWp0-9rW16Blc
LxytR2vp-1un56B2O-SuN5v7e9-ZDP96UIb

"""
