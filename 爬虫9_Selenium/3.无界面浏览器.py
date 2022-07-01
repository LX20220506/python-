from time import time
from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument('--headless') # 设置无界面模式
options.add_argument('--disable-gpu')  # 这个参数可以规避谷歌的部分bug

# 根据配置，创建谷歌浏览器对象
browser = webdriver.Chrome(options=options)

# 发起请求
browser.get("https://www.baidu.com/")

# 拿到按钮
kwl=browser.find_element_by_id("su")

# 输出按钮的value
print(kwl.get_attribute("value"))

#关闭当前界面，只有一个窗口
browser.close()
#关闭所有界面
browser.quit()

