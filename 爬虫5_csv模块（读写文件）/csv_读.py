import csv

# 读取普通csv文件
with open("eggs.csv","r",newline="") as f:
    spamreader = csv.reader(f,delimiter=" ",quotechar="|")
    for row in spamreader:
        print(",".join(row))


# 读取字典形式的csv文件
with open("names.csv","r",newline="") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["first_name"],row["last_name"])