import random
import time
from urllib import parse, request
from fake_useragent import UserAgent

## 定义一个爬虫类
class PaChong(object):

    ## 构造函数,设置初始url
    def __init__(self):
        self.url='http://tieba.baidu.com/f?{}'


    ## 1.请求网页，并读取，传统三步
    def get_html(self,url):
        ## 定义UA
        header={
            "User-Agent":UserAgent().firefox
        }

        ## 定义请求内容
        res=request.Request(url=url,headers=header)
        ## 获取响应
        response=request.urlopen(res)
        #windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
        #linux不会存在上述问题，可以直接使用decode('utf-8')解码
        html=response.read().decode("gbk","ignore") # 读取内容
        return html


    ## 2.解析函数，此处代码暂时省略，还没介绍解析模块
    def parse_html(self):
        pass


    ## 3.保存文件
    def save_file(self,html,filename):
        with open(file=filename,mode="w",encoding="utf-8") as f:
            f.write(html)


    ## 程序入口
    def run(self):
        name=input("输入搜索内容：")
        begin=input("输入起始页：")
        stop=input("输入结束页：")

        for page in range(int(begin),int(stop)+1):
            ## 分页参数
            pn=(page-1)*50
            ## 参数
            params={
                "kw":name,
                "pn":str(pn)
            }

            ## 进行编码,拿到编码后的参数
            codeParams = parse.urlencode(params)
            ## 拼接ulr
            url=self.url.format(codeParams)
            print("url:"+url)
            ## 发送请求
            html = self.get_html(url=url)

            ## 定义文件名称
            filename="{}-{}页.html".format(name,page)
            ## 保存文件
            self.save_file(html=html,filename=filename)

            ## 提示
            print('第%d页抓取成功'%page)
            ## 休眠2-4秒
            time.sleep(random.randint(2,4))

if __name__=="__main__":
    start = time.time() ## 开始时间
    spider=PaChong() ## 实例化爬虫对象
    spider.run()
    end=time.time() ## 结束时间
    ## 查看执行时间
    print('执行时间:%.2f'%(end-start))  #爬虫执行时间

