#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""代理和cookie维持"""
import requests


"""
代理是一种反反爬虫的手段
防止自己的ip泄露/追踪
http https socket4 socket5

proxies ={"HTTP":"202.55.5.209:8090"}
resp = requests.get(url=urla,headers=headers,proxies=proxies)
如果使用socks
proxies ={"HTTP":"socks5://202.55.5.209:8090"}

匿名代理:
知道你用代理,但是不知道你是谁

混淆代理:
知道你用代理,但是获取到的是假的ip地址

高匿代理:
无法发现你在使用代理

反爬虫侦测:
一段时间内ip访问频率
检查cookie,session,user-agent,referer,header等参数
服务器提供商
需要ip地址池更新
"""
"""处理session"""
def main():
    url="http://192.168.3.137/sqli-labs-master/Less-20/index.php"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
        #,"Cookie":"uname=admin"
    }
    data={"uname":"admin","passwd":"admin"}
    # #实例化session
    # session = requests.session()
    #
    # #发送post请求,提交用户名密码
    resp=requests.post(url,headers=headers,data=data)
    #
    # #此时session里面已经有cookie的信息了,可以直接用session去get登录后的任何界面
    # res = session.get(url,headers=headers)
    # print(res.content.decode("UTF-8"))

    #直接带着cookie做请求
    #cookie_dict = {"uname":"admin"}
    # resp = requests.get(url,headers=headers
    #                     #,cookies=cookie_dict
    # )

    #解码cookie
    cookies = requests.utils.dict_from_cookiejar(resp.cookies)
    print(cookies)
    #print(resp.content.decode('utf-8'))

    """
    如果要处理https网页
    ssl证书问题
    不去验证ssl证书
    一般会在post或者get里加一个
    verify=False
    
    """
    """
    超时参数
    设置3秒钟没反应,如果结合代理去使用,代理一段时间没反应,就可以从ip池删除了
    timeout=3
    """

    pass




if __name__ == '__main__':
    main()
