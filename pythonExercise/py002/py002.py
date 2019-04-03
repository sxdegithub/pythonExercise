# coding=utf-8

# https://github.com/Show-Me-the-Code/show-me-the-code
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# import sys
# sys.path.append(r'C:\Users\ssau\PycharmProjects\pythonExercise\py001')

import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()

# # 创建数据库
# cursor.execute("CREATE DATABASE IF NOT EXISTS COUPON DEFAULT CHARACTER SET UTF8MB4")


# 获取数据然后将数据插入到数据库
db.close()
