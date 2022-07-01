import re

#正则表达式分组
website="编程帮 www.biancheng.net"

# 注意此时正则表达式的 "." 需要转义因此使用 \.
pattern_1=re.compile("\w+\s\w+\.\w+\.\w+")
print(pattern_1.findall(website))  #['编程帮 www.biancheng.net']

# 提取匹配信息的第一项
pattern_2=re.compile("(\w+)\s\w+\.\w+\.\w+")
print(pattern_2.findall(website))  #['编程帮']

# 有两个及以上的()则以元组形式显示
pattern_3=re.compile("(\w+)\s(\w+\.\w+\.\w+)")
print(pattern_3.findall(website))  #[('编程帮', 'www.biancheng.net')]


