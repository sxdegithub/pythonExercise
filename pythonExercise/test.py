# coding=utf-8
# key = lambda item: item[1]
# print(key(2))

a = ("jpeg", "jpg")
b = ("jpeg", "jpg", "png")
i = "png"

if i not in a:
    print("i not in a ")
else:
    print("i is in a")

if i not in b:
    print("i not in b ")
else:
    print("i is in b")


str = '123132231213321312==321312213231123132'
print(str.strip('123'))