#导包,发起请求使用urllib库的request请求模块
from cgitb import html
from urllib import request
# urlopen()向URL发请求,返回响应对象,注意url必须完整
response=request.urlopen('https://www.baidu.com/')
#print(response)
#提取响应内容
html = response.read().decode("utf-8")
#打印响应内容
print(html)