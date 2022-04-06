import requests
from lxml import etree
import random

#页面内爬虫
def pachong(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
    # 网页的源码
    html_doc = resp.content.decode("utf-8")

    # 使用etree去转化html_doc,转化为了一个html的对象,此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    #print(html)
    dongmantitle = html.xpath('//div[@class="u-ct"]/p[@class="u-tt"]/text()')

    dongmanpic = html.xpath("//div[@class='lst']/a/img/@data-src")
    for i in range(len(dongmantitle)):
        print(dongmantitle[i]+'-------'+'http:'+dongmanpic[i])
    #for i in len(dongmantitle):
    #    print(dongmantitle[i]+'-----'+dongmanpic[i])

    #print(dongmantitle)
    #print(dongmanpic)
    pass

#发现下一页
def find_next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
    # 网页的源码
    html_doc = resp.content.decode("utf-8")

    # 使用etree去转化html_doc,转化为了一个html的对象,此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    #获得下一页链接
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    #创建完整的链接
    really_next_page="http://4399dmw.com"+next_page[0]
    #print(really_next_page)
    return really_next_page

def main():
    url="http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/"
    # while True:
    #     try:
    #         print("开始爬行的url:"+url)
    #         pachong(url)
    #         url = find_next_page(url)
    #         print('----------------------------')
    #     except:
    #         break
    # print("最后一页！")

    version_id = random.randint(50,100)
    os_type = ['Windows NT 10.0','Windows NT6.1','linux 10.0']




    """
    xpath语法
    
    xpath语法中,[1]就是第一个
    
    //a 当前html页面中所有的a标签
    //a/@href 当前html页面中所有a标签中的href的属性内容
    //a/text() 当前html页面中所有a标签中的文本内容
    //a/@src 拿到所有img标签中的src的内容
    //a//img/@src 拿到所有a标签下面的所有img标签中的src内容
    //img[@alt='超级呜呜侠']/@src 选择img标签中alt是某个值的标签并且提取src
    //div[@class="lst-item"][1]/a[3]/img/@src 选取页面中所有div并且class是lst-item,选择第一个
    并且选择第3个a标签中的img的src的内容
    //div[@class="lst-item"][1]/a[last()]/img a标签选择最后一个
    //p[text()='星路恋途第三季'] 查找所有p标签中,文字内容是xxx的
    //p[contains(text(),'超变')] 查找所有p标签中,包含某些文字的
    //p[@*] 页面中所有p标签凡是带有属性的
    //div[@class='lst-item'][1]/* 这里的*代表选择所有元素
    //div[@class='m-lst']/div[position()=1] 选择页面中所有class是m-lst的div中的第一个
    """


    pass

if __name__ == '__main__':
    main()

"""
反爬虫

通过user-agent
    ua="Mozilla/5.0 ("+random.choice(os_type)+"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987."+str(version_id)+" Safari/537.36",
    #ua=''.join(['Mozilla/5.0',random.choice(os_type),"bAppleWebKit/537.36 (KHTML, like Gecko)","Chrome/57.0.2987.",str(version_id)," Safari/537.36"])

通过Referer

通过cookie
考虑建立cookie池(多账户)

通过ip
使用代理ip等方法

验证码
考虑写程序识别验证码,打码平台

通过自定义字体
1.有的网站通过审查元素字体无法显示,显示为口,考虑使用手机网络访问
2.通过字体偏移
ABCDEFG....
CDEFGHI....


"""