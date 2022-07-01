from cgitb import html
from unicodedata import name
from unittest.mock import patch
from urllib import request, parse

# 封装Url


def get_url(word):
    ## https://so.eastmoney.com/web/s?keyword=%E6%B1%BD%E8%BD%A6
    # url = "http://www.baidu.com/s?{}"
    url = "https://so.eastmoney.com/web/s?{}"
    # 此处使用urlencode()进行编码
    params = parse.urlencode(
        #{"wb": word}
        {"keyword": word}
    )

    # 返回拼接完成之后的url
    url=url.format(params)
    return url


def request_url(url,filename):
    print(filename)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
    }
    req = request.Request(url=url,headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")

    # 保存到本地  
    # with 相当于 try…except…finally
    # open() 操作文件的方法
    with open(file=filename,mode='w',encoding='utf-8') as f:
        f.write(html) # 写入文件


## 主程序入口
if __name__=="__main__":
    word=input("请输入搜索内容：")
    ## 拿到拼接编码后的url
    url = get_url(word=word)
    ## 增加文件后缀
    filename=word+".html"
    request_url(url=url,filename=filename)


