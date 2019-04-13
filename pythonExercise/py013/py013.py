# coding=utf-8
# 第 0013 题： 用 Python 写一个爬图片的程序,爬 这个链接里的日本妹子图片 :-)
# 链接地址:http://tieba.baidu.com/p/2166231880
# https://github.com/Show-Me-the-Code/show-me-the-code

# 想法(不一定对):
# 1.用requests模块去请求也页面
# 2.用正则去匹配图片的链接,保存下来
# 3.用requests模块将图片下载下来,保存在文件夹里

import re
import time

import requests


# 获取图片页面
def get_pic_page(url):
    heads = {"Accept": "application/json, text/javascript, */*; q=0.01",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
             }
    try:
        # unicode用text
        text = requests.get(url, headers=heads).text
        # 文件用content
        # content = requests.get(url, headers=heads).content

        # print("text -->{}".format(text))
        # print("content -->{}".format(content))

        return text
    except requests.HTTPError as e:
        print(e)
        return None


# 从返回的页面匹配图片链接
def get_pic_urls(text):
    pattern = re.compile('<img pic_type="0" class="BDE_Image" src="(\S*\.jpg)"', re.IGNORECASE)
    urls = re.findall(pattern, text)
    return urls


# 下载文件并保存
def dowload_pic(url):
    heads = {"Accept": "application/json, text/javascript, */*; q=0.01",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
             }
    name = url.split("/")[-1]
    try:
        pic = requests.get(url, headers=heads).content
        with open(name, mode="wb") as f:
            f.write(pic)
        print("保存{}成功".format(name))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2166231880"
    data = get_pic_page(url)
    print("jandan_text --->".format(data))
    # print("text --->".format(data))
    urls = get_pics(data)
    for i in urls:
        time.sleep(0.4)
        # print("{} --->{}".format(urls.index(i) + 1, i))
        dowload_pic(i)