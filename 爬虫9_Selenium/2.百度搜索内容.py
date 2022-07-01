from selenium import webdriver
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys
import time

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])#开发者模式
options.add_argument('--disable-gpu')  # 这个参数可以规避谷歌的部分bug

browser = webdriver.Chrome(options=options)

browser.get("https://www.baidu.com/")

# 在搜索框中输入内容
browser.find_element_by_id("kw").send_keys("python")

# 点击搜索
browser.find_element_by_id("su").click()


time.sleep(10)
# 百度页面好像不能使用js。可以将浏览器设置为开发者模式，等待几秒后可以拖动滚动条
# document.documentElement.scrollTop = document.documentElement.scrollHeight * 0.3
# 拖动滚动条
js="document.documentElement.scrollTop = document.documentElement.scrollHeight * 0.3"
#执行js代码
browser.execute_script(js)

# time.sleep(3)

# # 退出浏览器
# browser.quit()


