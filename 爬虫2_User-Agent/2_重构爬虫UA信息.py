from cgitb import html
from email import header
from urllib import request, response

url="http://httpbin.org/get"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
}

res=request.Request(url=url,headers=headers)

response = request.urlopen(res)

html =response.read().decode("utf-8")

print(html)
'''
{
  "args": {},
  "headers": {
    "Accept-Encoding": "identity",
    "Host": "httpbin.org",

    识别为Edge浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    "X-Amzn-Trace-Id": "Root=1-62982d92-4d072eba2b7e718a3d17ebd1"
  },
  "origin": "223.104.68.82",
  "url": "http://httpbin.org/get"
}
'''