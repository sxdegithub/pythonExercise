# coding=utf-8
# https://github.com/Show-Me-the-Code/show-me-the-code
# **第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import sys

import redis

sys.path.append("..py001")
from py001 import py001_a as gsc

"""
# # 测试生成的100条优惠券
# coupons = gsc.get_group(10)
# print("type of coupons is :{}".format(type(coupons)))
# for i in coupons:
#     print(i)
"""
# 连接redis数据库
# 生成数据
coupons = gsc.get_group(2)

connect = redis.StrictRedis(host="localhost", port=6379, db=0, password='foobared')
for i in coupons:
    key_values = (coupons.index(i), i)
    print(key_values)
    connect.set(coupons.index(i), i)
print(connect.get('name'))
