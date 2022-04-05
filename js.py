#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""json"""
"""
爬虫不一定整站爬行,还可以请求接口

结构化数据:
json,xml

处理方式:直接转化为python类型

大多数手机版网页可能是json数据

审查元素--network--response看到

有的时候在访问json页面可能发生错误,因为有可能碰到了反爬虫程序,考虑是不是referer缺失等问题

json数据特征

{
 “class1”:
  “name1”:"xm",
  "name2":"xl"
 "class2":
  
}
"""
import requests
import json
def main():
    url = "https://json.tewx.cn/user/API_kdd531mytfdzm06i?sdAS1dsnuUa3sd=190001&Jsdh4bajs99dii=sohpuisypf4nfaei"
    resp = requests.get(url=url)

    content=resp.content.decode("utf-8")
    #把字符串变成字典
    shujv = json.loads(content)
    print(type(content))
    print(type(shujv))
    print(shujv["data"]["JSON"]["mydata"]["name"])

    pass

if __name__ == '__main__':
    main()


