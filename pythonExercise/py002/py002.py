# coding=utf-8

# https://github.com/Show-Me-the-Code/show-me-the-code
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# 导入..py001/里面的py001_a文件

import sys
sys.path.append(r'C:\Users\ssau\PycharmProjects\pythonExercise\py001')
from py001 import py001_a as gsc
import pymysql

connect = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db="interviews")
cursor = connect.cursor()

# # 创建数据库
# cursor.execute("CREATE DATABASE IF NOT EXISTS COUPON DEFAULT CHARACTER SET UTF8MB4")

"""
# 测试生成的100条优惠券
coupons = gsc.get_group(10)
print("type of coupons is :{}".format(type(coupons)))
for i in coupons:
    print(i)
"""

# 获取数据然后将数据插入到数据库
# 获取n条优惠券
coupons = gsc.get_group(200)
try:
    for i in coupons:
        sql = "INSERT INTO coupon (coupon_number) VALUES(%s)"
        # print("插入的sql语句:{}".format(sql))
        cursor.execute(sql, i)
        connect.commit()
        print("插入成功{}条".format(coupons.index(i)+1))

except pymysql.Error as e:
    print(e)
    connect.rollback()

cursor.close()
connect.close()
