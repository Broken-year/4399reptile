#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
bs的使用
"""

import requests
import json
#Beautiful Soup代替正则表达式
from bs4 import BeautifulSoup

def pachong(page):
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")

    # 使用bs处理网页源代码
    soup = BeautifulSoup(html_doc)
    list = soup.find('div', class_='lst').find_all('a', class_='u-card')

    for item in list:
        # 取出所有list中每一项的细节
        name = item.find('p', class_='u-tt').get_text()
        # 取出图片地址
        pic_url = item.find('img').get('data-src')
        print(name + "---http:" + pic_url)
    pass

def main():

    #url = "http://www.4399dmw.com/donghua/"




    #找到class='m-hd'的div标签
    #print(soup.find('div',class_='m-hd'))
    #print('------------------------')
    #找到所有的a标签并且class='u-card'的,放在list里,取出第几个
    #get_text()获得里面的文本,strip()去掉空格
    #print(soup.find_all('a',class_='u-card')[3].get_text().strip())

    #获取页面中有多少个这种元素
    #number = len(soup.find_all('a',class_='u-card'))
    #print(number)
    #for i in range(number):
        #获取某个元素的文字内容
    #    print(soup.find_all('a', class_='u-card')[i].get_text().strip())
    #print('--------------------')
    #查找所有div下id='j-anime-nav-collect'的标签内容,放在一个list里
    #类名前加点，id名前加#
    #print(soup.select("div > #j-anime-nav-collect"))
    #print('--------------------------')

    #print(soup.select("ul > .item")[1].get_text())
    #print('-----------------')

    # #取出网页的标题
    # print(soup.title.string)
    # print('------------------')
    #
    # #取出所有的img标签,放在一个list里
    # print(soup.find_all("img"))
    # print('------------------')
    #
    # #找到第一个class='u-tt'的,无视标签
    # print(soup.find(class_="u-tt").get_text())
    # print('----------------')

    # for i in range(5):
    #     print("爬虫到了第"+str(i)+"页")
    #     pachong(i)
    print('--------------------')

    url="http://www.4399dmw.com/huoying/donghua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")

    # 使用bs处理网页源代码
    soup = BeautifulSoup(html_doc)
    list=soup.find_all("div",class_="works__info")[3].find_all('a')
    for item in list:
        print(item.text)

    pass



if __name__ == '__main__':
    main()