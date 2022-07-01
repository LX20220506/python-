import csv

# 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象
with open("eggs.csv","w",newline="") as f:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格
    # quotechar 表示引用符
    # writerow 单行写入，列表格式传入数据
    spamwriter = csv.writer(f,delimiter=" ",quotechar="|")
    spamwriter.writerow(["www.biancheng.com"]*5+["how are you"])
    spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])

# 同时写入多行数据
with open('aggs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 注意传入数据的格式为列表元组格式
    writer.writerows([('hello','world'), ('I','love','you')])


# 使用字典类的形式写入数据
with open("names.csv","w",newline="") as f:
    # 构建字段名称，也就是key
    fieldnames ={"first_name","last_name"}
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    # 写入字段名，当做表头
    writer.writeheader()
    # 多行写入
    writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},{'first_name': 'Lovely', 'last_name': 'Spam'}])
    # 单行写入
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

