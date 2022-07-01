from hashlib import md5
import random
import requests
import time

"""
var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
        }
    };
"""

class YouDaoSpider(object):
    def __init__(self):
        # 默认url https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
        # 要将“_o”去掉，这是一种反爬虫策略
        # url一定要写抓包时抓到的POST请求的提交地址，但是还需要去掉 url中的“_o”，
        self.url="https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"


     # 获取lts时间戳,salt加密盐,sign加密签名
    def get_lts_salt_sign(self,word):
        lts = int(round(time.time() * 1000))# 13位时间戳
        # 时间戳后加一位随机数
        salt = int(str(round(time.time() * 1000))+str(random.randint(0,9)))

        # 加密参数
        # 创建加密对象
        secret=md5()
        string = "fanyideskweb" + word + str(salt) + "Ygy_4c=r#e#4EX^NUGUc5"
        secret.update(string.encode())
        sign = secret.hexdigest()
        return lts,salt,sign

    
    def attack_yd(self,word):
        header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }

        lts,salt,sign=self.get_lts_salt_sign(word=word)
        
        # 拼接请求参数
        data={
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "bdc0570a34c12469d01bfac66273680d",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }

        #使用 reqeusts.post()方法提交请求
        response=requests.post(url=self.url,headers=header,data=data)

        # res.json() 将json格式的字符串转为python数据类型
        # 客户端与服务器数据交互以json字符串传递，因此需要将它转换为python数据类型
        res = response.json()
        print(res)
        # 查看响应结果response  res:{"translateResult":[[{"tgt":"hello","src":"你好"}]],"errorCode":0,"type":"zh-CHS2en"
        print("翻译结果为："+res["translateResult"][0][0]["tgt"])

    
    def run(self):
        word=input("输入需要翻译的内容：")
        self.attack_yd(word=word)


if __name__=="__main__":
    spider=YouDaoSpider()
    spider.run()




