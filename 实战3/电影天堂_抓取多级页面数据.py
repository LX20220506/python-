from cgitb import html
from urllib import request, response
import pymysql
import re
from fake_useragent import UserAgent
from hashlib import md5

# https://www.dytt8.net/html/gndy/dyzz/index.html
# https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
# https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
# https://www.dytt8.net/html/gndy/dyzz/list_23_3.html


class movieSpider(object):
    def __init__(self):
        self.url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
        # 创建数据库连接对象
        self.db = pymysql.connect(
            host="localhost", user="root", password="123456", database="movieskydb")
        # 创建游标对象，执行sql命令
        self.cursor = self.db.cursor()

    # 请求页面，并保存
    def get_html(self, url):
        headers = {
            "User-Agent": UserAgent().firefox
        }
        res = request.Request(url=url, headers=headers)
        response = request.urlopen(res)
        html = response.read().decode('gb2312', 'ignore')

        return html

    # 通过正则表达式解析数据
    def parse_html(slft, zhengZe, html):
        pattern = re.compile(zhengZe, re.S | re.M)
        list = pattern.findall(html)
        return list

    # 保存数据到数据库
    def save_data(slft, list):
        sql = "insert into movieinfo values(%s,%s)"
        slft.cursor.execute(sql, [list[1],list[0]])
        slft.db.commit()

    # 判断是否存在该数据
    def check_movie(slft, url):
        # 生成MD5对象
        secret = md5()
        # 加密url
        secret.update(url.encode())
        # 提取十六进制的加密串
        finger = secret.hexdigest()

        sql = "select finger from request_finger where finger=%s"
        r = slft.cursor.execute(sql, finger)

        # 判断数据库中是否存在该数据
        if not r:
            # 若不存在，则添加该数据
            sql = "insert into request_finger values(%s)"
            slft.cursor.execute(sql, finger)  # 执行sql
            slft.db.commit()  # 提交命令
            return True

        return False

    def run(slft):
		## 拿前两页的数据
        for i in range(1, 3):
            html = slft.get_html(slft.url.format(i))
            zhengZe = '<table.*?class="tbspan".*?<a href="(.*?)".*?</table>'
			## 拿到电影的详情页面
            url_list = slft.parse_html(zhengZe=zhengZe, html=html)
			
			## 遍历详情页面，拿到电影播放路径
            for link in url_list:

                html = slft.get_html("https://www.dytt8.net"+link)
                zhengZe = '<a target="_blank" href="(.*?)".*?磁力链\s+(.*?)\.'
                movie_list = slft.parse_html(zhengZe=zhengZe, html=html)

                for info in movie_list:
                    if(slft.check_movie(info[0])):
                        slft.save_data(info)


if __name__ == "__main__":
    spider = movieSpider()
    spider.run()
