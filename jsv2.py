#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""json"""
import requests
import json
#Beautiful Soup代替正则表达式
from bs4 import BeautifulSoup

#美化打印
from pprint import pprint


"""
生成网站
https://www.onlinedatagenerator.com/
"""
def main():
    url="http://127.0.0.1/test1.json"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer":"http://www.baidu.com"
    }
    resp = requests.get(url=url,headers=headers)
    json_str = resp.content.decode("utf-8")
    #print(json_str)
    ret1 = json.loads(json_str)
    #print(ret1['objects'][4]['EmailAddress'])
    #pprint(ret1)
    #print(ret1)
    #保存
    """
    with open("./4399/jstest.txt","w",encoding="utf-8") as f:
        #ensure_ascii=False 可以显示中文,indent=2把子节点向后移2个空格
        
        f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
    """
    #读取本地json文件
    with open("./4399/jstest.txt","r",encoding="utf-8") as f:
        ret2 = json.load(f)
        print(ret2)
    pass


if __name__ == '__main__':
    main()