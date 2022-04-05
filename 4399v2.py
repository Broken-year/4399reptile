#! /usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from retrying import retry

#如果失败就请求3次,执行3次,如果还失败就报错,可以配合try
@retry(stop_max_attempt_number=3)
def qingqiu(inurl):
    url = inurl
    print("开始请求网站")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
    res = requests.get(url=url,headers=headers)
    with open("./4399/4399test.txt","wb+") as f:
        f.write(res.content)
    print("请求成功")
    pass


def main():
    try:

        qingqiu("http://www.4399dmw.comx/search/dh-1-0-0-0-0-0-0/")
    except:
        print("no")
    pass

if __name__ == '__main__':
    main()