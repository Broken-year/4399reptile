import requests
"""
selenium
web自动化测试工具
https://npm.taobao.org

chromedriver

https://vikyd.github.io/download-chromium-history-version/#/
"""

from selenium import webdriver
#引入键盘按键包
from selenium.webdriver.common.keys import Keys

#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def main():
    #设置手机型号
    #mobileEmulation={'deviceName':'iPhone 6/7/8'}

    #这种方法不建议
    # mobileEmulation={
    #     "deviceMetrics":{
    #         "width":350,
    #         "height":200,
    #         "pixelRatio":3.0,
    #         "touch":False
    #     }
    #}
    #指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    #chromeium浏览器的主程序位置
    location =r".\chromedrive\chrome-win\chrome.exe"
    #在options增加读取位置
    options.binary_location = location
    #使用手机浏览
    #options.add_experimental_option('mobileEmulation',mobileEmulation)

    #加代理http https socks4 socks5
    #options.add_argument('--proxy-server=%s'%'sock4://1.2.3.4:54321')


    # 使用静默模式
    # 不跳出浏览器,还去操作
    #options.add_argument("headless")

    service = Service(r".\chromedrive\chromedriver.exe")

    #更改浏览器语言
    #options.add_argument("--lang=en-US")
    driver = webdriver.Chrome(service=service,options=options)


    #使用get方法打开一个网站
    #driver.get("http://4399dmw.com/donghua/")


    #根据id找到对应的目标,并且输入什么设备
    #现在不推荐用这种方法了
    #driver.find_element_by_id("j-input").send_keys("赛尔号")
    #driver.find_element(By.ID,"j-input").send_keys("赛尔号")
    #找到按钮
    #driver.find_element(By.XPATH,"//button[@class='banner__btn']").click()
    #获取当前页面地址(尚未切换标签)
    # print(driver.current_url)
    # print('---------------------')
    #
    # #获取当前页面源码
    # print(driver.page_source)
    # print('---------------------')
    # #获取当前页面cookie
    # print(driver.get_cookies())
    # print('------------------')

    # time.sleep(2)
    # #刷新页面
    # driver.refresh()

    # ret = driver.find_elements(By.XPATH,"//div[@class='lst-item']/a/div/p")
    # print(ret)

    #点击下一页
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    # # driver.find_element(By.XPATH,"//a[contains(text(),'下一页')]").click()
    # driver.find_element(By.ID,'j-input').send_keys("AAAAAA")
    # #组合键输入
    # driver.find_element(By.ID,'j-input').send_keys(Keys.CONTROL,'a')

    # action = ActionChains(driver).move_by_offset(70,120).click()
    # #开始执行
    # action.perform()
    # #鼠标移动回来并且执行
    # ActionChains(driver).move_by_offset(-70,120).perform()

    #选择多个元素爬取
    # for page in range(15):
    #     print("现在开始爬第"+str(page)+"页")
    #     res = driver.find_elements(By.XPATH,"//div[@class='lst']/a/div/p")
    #
    #     for i in range(len(res)):
    #         print(res[i].text)
    #     #点到下一页
    #     driver.find_element(By.XPATH, "//a[contains(text(),'下一页')]").click()

    #获取目标元素的html代码
    #html = driver.find_element(By.XPATH,"//a[contains(text(),'下一页')]").get_attribute("outerHTML")
    #print(html)

    #获取css
    #.value_of_css_property("background-image")

    # #获取登录位置,发现一个是link的,文字是text的element
    # dl=driver.find_element(By.LINK_TEXT,"登录")
    # #鼠标悬停
    # ActionChains(driver).move_to_element(dl).perform()

    logo = driver.find_element(By.XPATH,"//div[@class='banner__main']/a")
    dl=driver.find_element(By.XPATH, "//a[contains(text(),'登录')]")

    #执行点击
    #方法1
    ActionChains(driver).click(logo).perform()

    #方法2
    action=ActionChains(driver)
    action.click(logo)
    time.sleep(2)
    action.click(dl)
    action.perform()

    time.sleep(5)
    # 关闭webdriver
    driver.quit()

    pass


if __name__ == '__main__':
    main()