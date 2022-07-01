import requests

# get请求的使用
response=requests.get("https://www.baidu.com/")
print(response) # <Response [200]>

# get请求+请求参数
data={
    "name":"编程帮",
    "url":"www.biancheng.net"
}
response=requests.get("http://httpbin.org/get",data)
#直接拼接参数也可以
#response = requests.get(http://httpbin.org/get?name=gemey&age=22)
#调用响应对象text属性，获取文本信息
print(response.text)

# post请求+请求参数
data={'from': 'zh',
        'to': 'en',
        'query': '编程帮www.biancheng.net你好'
        }
response=requests.post("https://fanyi.baidu.com",data)
print(response)


response = requests.get('http://www.baidu.com')
print(response.encoding)
response.encoding="utf-8"    #更改为utf-8编码
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url
print(response.headers)      # 打印头信息
print(response.cookies)      # 打印cookie信息
print(response.text)         #以字符串形式打印网页源码
print(response.content)      #以字节流形式打印