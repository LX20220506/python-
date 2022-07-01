from array import typecodes
from cgitb import html
from urllib import response
import requests
from fake_useragent import UserAgent
import re
import time
import random

# 1.拿到所有电影类型

# 2.通过类型进行抓取数据


class DouBanSpider(object):

    def __init__(self) :
        self.i=0



    # 设置ua
    def get_headers(self):
        headers = {
            "User-Agent": UserAgent().chrome
        }
        return headers



    # 获取电影的分类
    def get_menu(self):
        url = "https://movie.douban.com/chart"
        headers = self.get_headers()
        response = requests.get(url=url, headers=headers)
        response.encoding = "utf-8"
        html = response.text

        # 解析html,拿到电影的类型分类
        zhengze = "<a.*?type_name=(.*?)&type=(.*?)&"
        pares_html = re.compile(zhengze, re.S | re.M)
        menu_list = pares_html.findall(html)

        # 创建一个空字典，用于存放数据，格式：'科幻': '17'
        menu_dics = {}
        # 创建一个空字符串，拼接各个电影类型的名称
        menu_nameList = ""
        for item in menu_list:
            menu_nameList = menu_nameList+item[0]+"|"
            menu_dics[item[0]] = item[1]
        return menu_dics, menu_nameList



    # 拿到该电影的总条数
    def get_total(self, typeCode):
        url = "https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100:90".format(
            typeCode)
        headers = self.get_headers()
        response = requests.get(url=url, headers=headers)
        data = response.json()
        return int(data["total"])



    # 拿到指定类型的电影
    def get_movie(self, typeCode,start):
        url = "https://movie.douban.com/j/chart/top_list?"
        headers = self.get_headers()
        params = {
            "type": typeCode,
            "interval_id": "100:90",
            "action": "",
            "start": str(start),
            "limit": "20"
        }

        response = requests.get(url=url,headers=headers,params=params)
        data = response.json()
        for movie in data:
            info={}
            info["title"]=movie["title"]
            info["score"]=movie["rating"][0]
            print(info)
            self.i+=1



    def run(self):
        menu_dics, menu_nameList=self.get_menu()
        print(menu_nameList)
        type=input("请输入想要查看的类型：") # 输入电影类型
        typeCode = menu_dics[type] # 拿到对应类型的编号
        total=self.get_total(typeCode=typeCode) # 拿到类型电影的总数
        # 因为页面是动态的，模拟向下滚动滑轮。当向下滑动时，会发现页面进行了异步请求
        for start in range(0,total,20):
            self.get_movie(start=start,typeCode=typeCode)
            time.sleep(random.randint(1,3)) # 随机休眠1-3秒



if __name__ == "__main__":
    spider = DouBanSpider()
    spider.run()
    print("电影总数量："+str(spider.i))
