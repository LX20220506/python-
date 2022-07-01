import re

html="""
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""


# 贪婪匹配，re.S可以匹配换行符
# 创建正则表达式对象
pattern_1=re.compile("<div><p>.*</p></div>",re.S)
# 匹配HTMLX元素，提取信息
data_1=pattern_1.findall(html)
print(data_1)# ['<div><p>www.biancheng.net</p></div>\n<div><p>编程帮</p></div>']


#非贪婪模式匹配，re.S可以匹配换行符
pattern_2=re.compile("<div><p>.*?</p></div>")
data_2=pattern_2.findall(html)
print(data_2)# ['<div><p>www.biancheng.net</p></div>', '<div><p>编程帮</p></div>']
