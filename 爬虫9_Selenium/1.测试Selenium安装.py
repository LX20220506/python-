# 导入seleinum webdriver接口
from selenium import webdriver
import time

# 创建Chrome浏览器对象
browser = webdriver.Chrome()

# 创建Chrome浏览器对象
browser.get("http://www.baidu.com/")

#阻塞3秒
time.sleep(3)

#阻塞3秒
browser.quit()

