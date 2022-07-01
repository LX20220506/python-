import pymysql

# 创建数据库连接对象
db=pymysql.connect(host="localhost",user="root",password="123456",database="maoyandb")

# 创建一个游标对象，用于执行sql命令
cursor = db.cursor()

## 添加数据_1：
    # 定义sql命令
sql_1 ="insert into filmtab(name,star,time)  value('%s','%s','%s')"%('我不是药神','我不是药神','2018-07-05')
    # 执行sql命令
cursor.execute(sql_1)

## 添加数据_2：
    # 定义sql命令
sql_2="insert into filmtab(name,star,time)  value(%s,%s,%s)"
    # 执行sql命令
cursor.execute(sql_2,['肖申克的救赎', '蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿', '1994-09-10(加拿大)'])


## 添加数据_3：添加多行数据
# sql语句执性，列表元组
info_list = [('我不是药神','徐峥','2018-07-05'),('你好,李焕英','贾玲','2021-02-12')]
sql_3="insert into filmtab(name,star,time)  value(%s,%s,%s)"
cursor.executemany(sql_3,info_list)

# 提交到数据库执行
db.commit()

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
