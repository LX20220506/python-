import requests
from fake_useragent import UserAgent

url = "https://img1.baidu.com/it/u=1807166483,1107331951&fm=253&fmt=auto&app=138&f=JPEG?w=641&h=401"
#定义浏览器ua信息
header={
    "User-Agent":UserAgent().ie
}
#读取图片需要使用content属性
html = requests.get(url,headers=header).content
#以二进制的方式下载图片
with open("E:\Python\python_log.jpg","wb") as f:
    f.write(html)