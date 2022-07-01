from cmath import e
import random
import re
import time
from urllib import request,parse
from fake_useragent import UserAgent
import csv
#https://www.maoyan.com/board/4
# ?index=10&signKey=935779043e0365e204cf1e7406489ca3&sVersion=1&webdriver=false

#https://www.maoyan.com/board/4
# ?timeStamp=1654505157140&channelId=40011&index=10&signKey=58c8d47bcbc4d6f08322841d4e5e38ec&sVersion=1&webdriver=false

#https://www.maoyan.com/board/4
# ?offset=0


#https://www.maoyan.com/board/4
# ?timeStamp=1654504598435&channelId=40011&index=10&signKey=935779043e0365e204cf1e7406489ca3&sVersion=1&webdriver=false&offset=10

#https://www.maoyan.com/board/4?
# timeStamp=1654505015380&channelId=40011&index=9&signKey=fe8eb59d863a807e0dfa8bf9c6b687a8&sVersion=1&webdriver=false&offset=20

#https://www.maoyan.com/board/4?
# timeStamp=1654505157140&channelId=40011&index=10&signKey=58c8d47bcbc4d6f08322841d4e5e38ec&sVersion=1&webdriver=false&offset=40


#主要编写四个函数，分别是请求函数、解析函数、保存数据函数、主函数。

class movieSpider(object):
    def __init__(self):
        self.url="https://www.maoyan.com/board/4?{}"

    ## 请求函数
    def get_html(self,url):
        header={
            "User-Agent":UserAgent().firefox
        }
        res=request.Request(url=url,headers=header)
        response=request.urlopen(res)
        html=response.read().decode()
        self.parse_html(html)

    ## 解析函数
    def parse_html(self,html):
        pattern =re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">.*?主演：(.*?)\s+</p>.*?上映时间：(.*?)</p>',re.S|re.M)
        list = pattern.findall(html)
        print(list)
        print()
        self.save_html(list)

    ## 保存数据函数，使用python内置csv模块
    def save_html(self,list):
        with open("maoyan.csv","w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in list:
                L=[row[0].strip(),row[1].strip(),row[2].strip()]
                writer.writerow(L)
                

    
    ## 主函数
    def run(self):
        for i in range(0,11,10):
            params={
                "offset":str(i)
            }
            codeParams=parse.urlencode(params)
            self.get_html(url=self.url.format(codeParams))
            time.sleep(random.uniform(3,4))



if  __name__=="__main__":
    try:
        spider = movieSpider()
        spider.run()
    except Exception as e:
        print(e)
