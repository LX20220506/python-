from selenium import webdriver
import time
import pymysql
import selenium.webdriver.support.ui as ui

class JingDongSpider(object):

    def __init__(self) :
        # 浏览器配置
        options= webdriver.ChromeOptions()
        options.add_argument("--headless") # 无界面模式
        options.add_argument('--disable-gpu')  # 这个参数可以规避谷歌的部分bug
        self.browser=webdriver.Chrome(options=options)

        # 总数量
        self.i=0

    def get_html(self,word):
        self.browser.get("https://www.redup.cn/")
        time.sleep(1) # 等待2秒

    
    # 获取数据
    def get_data(self):

        li_list = li_list=self.browser.find_elements_by_xpath('//*[@class="comm-course-list"]//li') # 拿到所有的li标签

        info_list=[]
       
        for li in li_list:
            #构建空字典
            name=li.find_element_by_xpath('./div/div[4]/a/em').text.strip()
            price=li.find_element_by_xpath('./div/div[3]/strong/i').text.strip()
            pinglun=li.find_element_by_xpath('.//div[@class="p-commit"]/strong/a').text.strip()
            shop=li.find_element_by_xpath('./div/div[7]/span/a').text.strip()
            # 数据库一次添加多行数据需要 元组列表类型
            info=(name,price,pinglun,shop)
            info_list.append(info)

            self.i+=1 # 数量 加1
            print(info)


    




    def run(self):
        

            
        print(self.i)


        
if __name__=="__main__":
    spider = JingDongSpider()
    spider.run()