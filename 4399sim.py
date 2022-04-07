"""
模拟人类操作采集信息
"""
import requests
from selenium import webdriver
#引入键盘按键包
from selenium.webdriver.common.keys import Keys

#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#如果碰到了下拉框
from selenium.webdriver.support.ui import Select
"""
使用select包裹起来xpath查找到的select元素
select1 = Select(driver.find_element(By.XPATH,"//select[@class='year']"))
选择值是1999的
select1.select_by_value("1999")
"""


import time

def main():
    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    # chromeium浏览器的主程序位置
    location = r".\chromedrive\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    # 设置手机型号
    mobileEmulation={'deviceName':'iPhone SE'}
    # 使用手机浏览
    #options.add_experimental_option('mobileEmulation',mobileEmulation)


    service = Service(r".\chromedrive\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    #driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")

    #拖拽操作

    #拖拽操作需要使用xpath或者其他方法找到起始位置和终点位置
    # first_tar = driver.find_element(By.XPATH,"//span[contains(text(),'喜羊羊与灰太狼之决战次时代')]")
    # second_tar = driver.find_element(By.XPATH,"//a[contains(text(),'动画')]")
    # action = ActionChains(driver)
    # action.drag_and_drop(first_tar,second_tar).perform()

    #鼠标点击像素操作
    #把鼠标移动到某个特定的地方,然后执行
    # ActionChains(driver).move_by_offset(50,300).key_down().perform()
    # ActionChains(driver).move_by_offset(-50, 300).perform()

    #鼠标移动到某个元素
    #ele = driver.find_element(By.XPATH,"//p[@class='u-tt']")
    #ActionChains(driver).move_to_element_with_offset().context_click().perform()


    """
    click() 点击鼠标左键
    click_and_hold() 点住鼠标左键不放
    context_click() 点击鼠标右键
    double_click() 双击鼠标左键
    drag_and_drop_by_offset(target,x,y) 把鼠标拽到某个坐标然后松开
    key_down() 按下一个键
    key_up() 松开一个键
    move_to_element() 移动到某个元素的位置
    move_to_element_with_offset(target,x,y) 移动到某个元素的相对xx的位置,以找到元素的左上角作为0
    """

    # #新建标签页
    # js = 'window.open("http://www.baidu.com")'
    # driver.execute_script(js)
    # # print(driver.current_url)
    # #查看当前有多少个窗口,并且句柄是什么
    # # print(driver.window_handles)
    # #切换选项卡 0就是原来的
    # driver.switch_to.window(driver.window_handles[1])
    # print(driver.current_url)

    driver.get("http://127.0.0.1/index.html")

    #处理弹窗
    driver.switch_to.alert.accept()
    time.sleep(2)

    #关于iframe的处理
    #方法1
    #寻找到iframe的位置
    # find_div = driver.find_element(By.CSS_SELECTOR,"#waimian>iframe")

    #方法2
    find_div = driver.find_element(By.TAG_NAME,"iframe")

    #让driver切换到iframe所代表的网页中
    driver.switch_to.frame(find_div)

    ele = driver.find_elements(By.XPATH,"//div[@class='lst']/a/div/p")
    for i in range(len(ele)):
        print(ele[i].text)

    #释放iframe,回到主页面上
    driver.switch_to.default_content()

    print('--------------------')

    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")

    #获取标签下的文字
    res=driver.find_elements(By.XPATH,"//div[@class='u-ct']")
    for i in range(len(res)):
        title = res[i].find_element(By.XPATH,"./p[@class='u-tt']").get_attribute('innerText')
        print(title)
    print('--------------------')





    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass

if __name__ == '__main__':
    main()
