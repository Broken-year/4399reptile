#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""爬虫小实验"""
import requests


def main():
    url="http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
    url_list=[]
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
    for i in range(1):
        # url_list.append(url.format(i))
        #
        # #遍历地址列表并且发送get请求,然后保存
        # for item in url_list:
        #     resp = requests.get(url=item,headers=headers)
        #     with open("a"+str(i)+".txt","wb+") as f:
        #         #写入文件
        #         f.write(resp.content)

        #代理 http https socket4 socket5
        proxies ={"HTTP":"202.55.5.209:8090"}
        urla = url.format("1")
        print(urla)
        resp = requests.get(url=urla,headers=headers,proxies=proxies)
        with open("./4399/a.txt","wb+") as f:
            f.write(resp.content)
    pass

if __name__ == '__main__':
    main()