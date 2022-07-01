# 引用包
from urllib import request
#   通过向 HTTP 测试网站（http://httpbin.org/）发送 GET 请求来查看请求头信息，从而获取爬虫程序的 UA
'''
注意：httpbin.org 这个网站能测试 HTTP 请求和响应的各种信息，
比如 cookie、IP、headers 和登录验证等，
且支持 GET、POST 等多种方法，对 Web 开发和测试很有帮助。
'''

# 开始请求 拿到响应
response = request.urlopen("http://httpbin.org/get")

# 读取信息
html = response.read().decode()

print(html)
## 响应信息
# {
#   "args": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.10", # UserAgent信息包含在请求头中！
#     "X-Amzn-Trace-Id": "Root=1-629829ea-62d83dc735c8e6c278f52831"
#   },
#   "origin": "223.104.68.82",
#   "url": "http://httpbin.org/get"
# }
