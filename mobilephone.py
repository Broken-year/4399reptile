"""
模拟手机操作
"""
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
def main():

    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    # chromeium浏览器的主程序位置
    location = r".\chromedrive\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    # # 设置手机型号
    # mobileEmulation = {'deviceName': 'iPhone SE'}
    # # 使用手机浏览
    # options.add_experimental_option('mobileEmulation',mobileEmulation)
    #
    # #关闭w3c模式！！！非常重要,否则无法点击
    # options.add_experimental_option('w3c',False)

    driver = webdriver.Chrome(".\chromedrive\chromedriver.exe", options=options)

    # 使用get方法打开一个网站
    driver.get("http://4399dmw.com/donghua/")

    # #点击坐标操作
    # action = TouchActions(driver)
    # action.tap_and_hold(75,60).release(75,60).perform()
    """
    double tap 双击
    filck_element
    long_press 长按
    move 移动
    perform
    release 放开
    scroll 滚动
    tap 点击
    """


    time.sleep(5)

    #清楚input标签所有的value
    shell1=driver.find_element(By.XPATH,'//input[@id="j-input"]')
    driver.execute_script("arguments[0].value='';",shell1)




    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
