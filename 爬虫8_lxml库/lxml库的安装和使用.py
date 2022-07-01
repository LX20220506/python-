from lxml import etree

html="""
<div class="wrapper">
    <a href="www.biancheng.net/product/" id="site">website product</a>
    <ul id="sitename">
    <li><a href="http://www.biancheng.net/" title="编程帮">编程</a></li>
    <li><a href="http://world.sina.com/" title="新浪娱乐">微博</a></li>
    <li><a href="http://www.baidu.com" title="百度">百度贴吧</a></li>
    <li><a href="http://www.taobao.com" title="淘宝">天猫淘宝</a></li>
    <li><a href="http://www.jd.com/" title="京东">京东购物</a></li>
    <li><a href="http://c.bianchneg.net/" title="C语言中文网">编程</a></li>
    <li><a href="http://www.360.com" title="360科技">安全卫士</a></li>
    <li><a href="http://www.bytesjump.com/" title=字节">视频娱乐</a></li>
    <li><a href="http://bzhan.com/" title="b站">年轻娱乐</a></li>
    <li><a href="http://hao123.com/" title="浏览器">搜索引擎</a></li>
    </ul>
</div>
"""

# 提取所有a标签内的文本信息
# 创建解析对象
pares_html_1=etree.HTML(html)
# 设置xpath表达式
xpath_bds_1="//a/text()"
# 开始匹配
r_list_1= pares_html_1.xpath(xpath_bds_1)
print(r_list_1)


#  获取所有href的属性值
# 创建解析对象
pares_html_2 =etree.HTML(html)
# 设置xpath表达式
xpath_bds_2="//a/@href"
# 开始匹配
r_list_2 = pares_html_2.xpath(xpath_bds_2)

print(r_list_2)

# 不匹配href=" www.biancheng.net/priduct"
# 创建解析对象
pares_html_3=etree.HTML(html)
# 设置xpath表达式
xpath_bds_3="//ul[@id='sitename']//a/@href"
# 开始匹配
r_list_3=pares_html_3.xpath(xpath_bds_3)
print(r_list_3)