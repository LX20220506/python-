import re
from sys import int_info

html="""
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
# 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
pattern_1=re.compile('<div.*?<a\stitle="(.*?)".*?"star">(.*?)</p>',re.S)

list=pattern_1.findall(html)

print(list)
# [('你好，李焕英', '\n主演：贾玲,张小斐,沈腾\n'), ('刺杀，小说家', '\n主演：雷佳音,杨幂,董子健,于和伟\n')]
print()

for info in list:
    print(info[0])
    print(info[1])
    print("*"*20)

# 影片名称： 你好，李焕英
# 影片主演： 主演：贾玲,张小斐,沈腾
# ********************
# 影片名称： 刺杀，小说家
# 影片主演： 主演：雷佳音,杨幂,董子健,于和伟
# ********************