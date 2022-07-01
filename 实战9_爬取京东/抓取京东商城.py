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

        # 创建数据库连接
        self.db = pymysql.connect(host="localhost",user="root",password="123456",database="JingDong") # 创建数据库连接对象
        self.cursor = self.db.cursor() # 创建执行sql命令对象

        # 总数量
        self.i=0

    def get_html(self,word):
        self.browser.get("https://www.jd.com/")
        time.sleep(1) # 等待2秒
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys(word)
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

    
    # 获取数据
    def get_data(self):
        # 拖动滚动条
        for i in range(1,10,3):
            x=i/10  # 控制滚动条进度
            # 拖动滚动条
            js="document.documentElement.scrollTop = document.documentElement.scrollHeight * {}".format(x)
            #执行js代码
            self.browser.execute_script(js)
            time.sleep(1) # 休眠

        time.sleep(2)
        # 解析结果，获取数据
        li_list = li_list=self.browser.find_elements_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li') # 拿到所有的li标签

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
        # 保存到mysql
        self.save_data(data=info_list)

    
    # 保存数据
    def save_data(self,data):
        sql="INSERT INTO `T-Shirt`(Name,Price,PingLun,Shop) VALUES (%s,%s,%s,%s)"
        self.cursor.executemany(sql,data)
        self.db.commit()



    def run(self):
        #word=input("请输入你想搜索的内容：")
        self.get_html('情侣服')
        
        while True:
            self.get_data()
            # 判断页面的“下一页”是否可以点击
            if self.browser.page_source.find('pn-next disabled')==-1: # 可以
                self.browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
                time.sleep(2)
            else:
                break

            
        
        self.cursor.close()
        self.db.close()
        print(self.i)


        
if __name__=="__main__":
    spider = JingDongSpider()
    spider.run()



    

    