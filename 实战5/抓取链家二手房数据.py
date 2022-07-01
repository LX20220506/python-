import requests
from fake_useragent import UserAgent
from lxml import etree

"""
https://bj.lianjia.com/ershoufang/pg1/
https://bj.lianjia.com/ershoufang/pg2/
https://bj.lianjia.com/ershoufang/pg3/
"""

class LianJiaSpider(object):
    def __init__(self):
        self.url="https://bj.lianjia.com/ershoufang/pg{}"

    # 获取html
    def get_html(self,url):
        # 定义请求头
        headers={
            "User-Agent":UserAgent().edge
        }
        # 请求信息
        response = requests.get(url,headers=headers)
        # 修改编码格式
        response.encoding="utf-8"
        # 拿到页面的源码
        html = response.text
        return html
    

    # 解析html
    def pares_html(self,html,xpath_bds):
        # 创建html的解析对象
        pares_html = etree.HTML(html)
        # 开始匹配传入的xpath表达式
        list = pares_html.xpath(xpath_bds)
        return list

    
    def run(self):
        # 创建自动类型的变量，接收数据
        data={}
        for i in range(1,3):
            url = self.url.format(str(i))
            html = self.get_html(url=url)

            # print(html)

            # 名称
            xpath_bds='//div[@class="positionInfo"]/a[1]/text()'
            name_list = self.pares_html(html=html,xpath_bds=xpath_bds)
            
            # 地址
            xpath_bds='//div[@class="positionInfo"]/a[2]/text()'
            address_list = self.pares_html(html=html,xpath_bds=xpath_bds)

            # 基本信息
            xpath_bds='//div[@class="houseInfo"]/text()'
            info_list = self.pares_html(html=html,xpath_bds=xpath_bds)

            # 总价
            xpath_bds='//div[@class="priceInfo"]/div[1]/span/text()'
            totalPrice_list = self.pares_html(html=html,xpath_bds=xpath_bds)

            # 每平方价格
            xpath_bds='//div[@class="priceInfo"]/div[2]/span/text()'
            price_list = self.pares_html(html=html,xpath_bds=xpath_bds)

            # 拼接数据
            for i in range(0,len(name_list)):
                data["name"]=name_list[i]
                data["address"]=address_list[i]

                # 1室1厅 | 92.47平米 | 南 | 精装 | 低楼层(共18层) | 2003年建 | 板楼
                info = str(info_list[i]).split('|') # info使用|分割完后，变成字符串数组，得到单个信息
                data["model"]=info[0]
                data["area"]=info[1]
                data["direction"]=info[2]
                data["perfect"]=info[3]
                data["floor"]=info[4]

                data["totalPrice"]=totalPrice_list[i]
                data["price"]=price_list[i]

                print(data)


if __name__=="__main__":
    spider=LianJiaSpider()
    spider.run()



    