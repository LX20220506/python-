'''
当 URL 路径或者查询参数中，带有中文或者特殊字符的时候，
就需要对 URL 进行编码（采用十六进制编码格式）。
URL 编码的原则是使用安全字符去表示那些不安全的字符。
'''
from urllib import parse


# 这是在百度中搜索“爬虫”后，复制下来的链接，
#https://www.baidu.com/s?
# ie=utf-8
# &f=8
# &rsv_bp=1&rsv_idx=1
# &tn=baidu
# &wd=%E7%88%AC%E8%99%AB    ### wd参数是要搜索的内容，复制后，被编码了 原来是“爬虫”
# &fenlei=256
# &rsv_pq=978f33f10006b89e
# &rsv_t=c65d7x1r5ijEDbe9cRoEgrQ1gylbTziHOIcz4PPIZbcD7gCa8dNPI50mgjK3
# &rqlang=en
# &rsv_enter=1
# &rsv_dl=ib&rsv_sug3=7
# &rsv_sug1=9
# &rsv_sug7=100

#构建查询字符串字典
query_string = {
'wd' : '爬虫'
}
#调用parse模块的urlencode()进行编码
result = parse.urlencode(query_string)
#使用format函数格式化字符串，拼接url地址
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

## 进行解码
string = '%E7%88%AC%E8%99%AB'
result = parse.unquote(string)
print(result)