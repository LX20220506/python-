import os
import requests
from fake_useragent import UserAgent
import re

#https://soso.nipic.com/?q=%E8%83%8C%E6%99%AF&g=0&page=4
#https://soso.nipic.com/?q=%E8%83%8C%E6%99%AF&g=0&page=5

## 百度的图片没法下，换个网站
class BaiDuImageSpider(object):
    def __init__(self):
        self.url="https://soso.nipic.com/?q={}&page={}"

    def get_image(selft,url,q,page):
        
        headers={
            "User-Agent":UserAgent().edge
        }

        # parameter={
        #     "q":q,
        #     "page":page
        # }
        
        # 获取页面源码
        response = requests.get(url=url,headers=headers)
        response.encoding="utf-8"
        html = response.text
        
        # 解析源码，获取数据py
        zhengze='data-original="(.*?)"'
        list = selft.parse_html(zhengze=zhengze,html=html)
        
        # 创建目录，用于保存图片
        directory = 'E:/Python/爬虫Demo/实战4/image/{}/{}/'.format(q,page)
        # 如果目录不存在则创建，此方法常用
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 将图片保存到本地
        i=1
        for imageUrl in list:
            filename="{}{}_{}.jpg".format(directory,q,str(i))
            print(filename)
            selft.save_image(url="http:"+imageUrl,filename=filename)
            i+=1

    # 保存图片
    def save_image(self,url,filename):
        #拿到image的字节流形式
        image = requests.get(url).content
        print(filename)
        #以二进制的方式下载图片
        with open(filename,"wb") as f:
            f.write(image)

    # 解析源码
    def parse_html(self,zhengze,html):
        pattern = re.compile(zhengze)
        list = pattern.findall(html)
        return list

    def run(self):
        q = input("输入想下载的图片：")
        start = int(input("输入起始页："))
        end = int(input("请输入截止页："))+1

        for i in range(start,end):
            url = self.url.format(q,i)
            self.get_image(q=q,url=url,page=i)

        

if  __name__=="__main__":
    spider = BaiDuImageSpider()
    spider.run()




# zhengze='data-original="(.*?)"'

# pattern = re.compile(zhengze)
# list = pattern.findall(html)
# print(list)
# for i in list:
#      print(i)
