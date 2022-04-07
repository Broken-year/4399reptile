"""
cookie滑块标签操作
"""
import requests
from selenium import webdriver
#引入键盘按键包
from selenium.webdriver.common.keys import Keys
#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#超时操作
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web():
    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()

    # 某些网站会识别selenium,下面这个屏蔽网站对selenium的识别
    options.add_experimental_option('excludeSwitches',['enable-automation'])

    # chromeium浏览器的主程序位置
    location = r".\chromedrive\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone SE'}
    # 使用手机浏览
    # options.add_experimental_option('mobileEmulation',mobileEmulation)

    service = Service(r".\chromedrive\chromedriver.exe")

    # #图片不加载
    # prefs = {
    #     'profile.default_content_setting_values':{
    #         'images':2
    #     }
    # }
    # options.add_experimental_option('prefs',prefs)



    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    #如果10s页面还没加载出来,就抛出一个异常,需要配合try来做
    #driver.set_page_load_timeout(10)

    #隐性等待,全局查找页面元素的等待时间,如果这个时间没有找到指定元素,就抛出异常,全局做一次就好
    driver.implicitly_wait(10)

    #显性等待,使用频率最高的元素超时设置
    #如果10秒内页面加载的是这个,就返回true,不是就报错
    # a=WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(u'动画片-动画电影-少儿动画片-动画片大全免费在线观看-4399动漫网'))

    # target1=driver.find_element(By.XPATH,"//div[@class='lst']/a[3]")
    # ActionChains(driver).click(target1).perform()
    # #切到第一个标签
    # driver.switch_to.window(driver.window_handles[0])
    #
    # target2=driver.find_element(By.XPATH,"//div[@class='lst']/a[4]")
    # ActionChains(driver).click(target2).perform()
    # driver.switch_to.window(driver.window_handles[1])
    # #关闭当前切到的标签
    # driver.close()

    """
    EC.title_is 有这个东西
    EC.title_contains 包含
    EC.presence_of_element_located 能用By.xxx 
    EC.invisibility_of_element 元素被可见(高宽都>0)
    EC.text_to_be_present_in_element 匹配语法是哪个
    """
    # print(a)
    """
    until用来检测指定的元素是否出现,如果在超时的时间内出现就返回选择器的信息,否则就报
    TimeOutException
    until_not用来检测指定的元素是否消失,如果在超时时间内消失返回True,否则报
    TimeOutException
    """


    time.sleep(10)
    driver.quit()
    pass
def main():

    #浏览器操作
    # driver.get("http://www.4399dmw.com/dh/cjdzz/")
    # #后退
    # driver.back()
    # time.sleep(2)
    # #刷新
    # driver.refresh()
    # #前进
    # driver.forward()
    #最大化
    # driver.maximize_window()

    #查看cookie
    #cookie = driver.get_cookies()
    #print(cookie)
    #增加cookie
    #driver.add_cookie({'name':'xiaoming','key':'9988'})

    #清除所有cookie
    #driver.delete_all_cookies()

    #拖动滑块操作
    #拖动滑块到底部
    # js = "document.documentElement.scrollTop=10000"
    # driver.execute_script(js)

    #截图操作
    # driver.get_screenshot_as_file("./abc.jpg")
    #base64
    # a = driver.get_screenshot_as_base64()
    # print(a)
    #指定部分截图
    # pic = driver.find_element(By.XPATH,'//div[@class="lst"]/a[3]')
    # pic.screenshot('./chiji.png')

    #超时操作系列
    try:
        web()
    except:
        print('this is bad')





    pass

if __name__ == '__main__':
    main()