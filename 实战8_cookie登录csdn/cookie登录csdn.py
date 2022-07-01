from cgitb import html
from cmath import inf
from email.mime import image

import requests

from requests import request

import requests
from lxml import etree

class CSDNSpider(object):
    def __init__(self):
        self.url="https://bizapi.csdn.net/blog-console-api/v1/data/blog_statistics"
    
    def get_data(self):
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "cookie":"uuid_tt_dd=10_37481524260-1655194086700-715642; dc_session_id=10_1655194086700.371760; c_dsid=11_1655194088904.043678; c_first_ref=default; c_segment=10; hide_login=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1653869989,1653894870,1654562452,1655079392; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37481524260-1655194086700-715642!5744*1*weixin_48246845; is_advert=1; dc_sid=d614e3030141b0085a04cab91c4be339; SESSION=6ea810d8-b7af-46fe-9249-9914153fe697; acw_sc__v2=62a84256d450e41aabfe40f797feefa8f7f8b36a; ssxmod_itna=QqmxgDBQG=i=dDIx0dD=G7IHHM80eqYeeTK=Y8Dl1cQxA5D8TD6WhD=rDrnDhDBKa/Ajx4eaKtR34R3eiA4OtHDU4i8DCLGpoD44GTDt4DTD34DYDirQGy8qBQDjxAQDjGKGaDfTtGcDYjjiM4DChG4h7=DI4GMU4DuDGUPwxiDYwtDmq=DY+tDjM3DKwtKyqD2zOu9DYpcGDDltSYDK4+t=LcF2u2YEnRQglb=X4n=kaPy+LtnDYEjK60cFztS8av3WhG3IY5AIAxFKB4e/i+PSzGtYsxGQ8+xDf4gXD4GDNwCn5DAjNwdmxbYD; ssxmod_itna2=QqmxgDBQG=i=dDIx0dD=G7IHHM80eqYeeTK=YD6pzxCuDDsHkqDLG9WLi9Dqasx7dsDxFrF634r/MbXGeD/jKGF4FgPrLcYGik0xi/Fkrjsk1/cF46rX7Uf6=8HYpUZuYDUBkTq8=DY4/3An4R3yKboL3jvFfRpZGOrvjuKLW8UCjfUgUl+ISo3L8+XrMjvPqQ6=xab31wXNdPIdcd6runnBmCWgI461ER6zUQr7fwfQMOTWL631sFOMRaRdw9HMFQ5HKM+wK=FXgMj4PI7Iml0KcbE3lSQvNl2ntwkRh9U6A+Mh95ZVENwoEZOtOWGkAwKl5NWqS=m3ZdOePg0vkOemae=Er/Aeo/AMxqi3oUEU8iLAlwxCx+epqQmsYUhpe44PZaYZgb48w34qf7wpgT33EseWnWuT+5Uii1FXpIIwzxXDKRQDKR2vrLQOojSIzamaI4DQ94YDe+GQ3exFiGYiP4n4I8TKidnwkLqxS0GIxiAL1Li13GQ8bYDwWcx47osXihL23cTdWCTmSwALCSRMbdiAjws2IyMmHi1FA=SDezbh90A=G=42G=44Woe+OY+2+svjV2oD08DiQ2C9FiDigwOA7jYw7Mq4mPERbYl6Z8DRgF2YaGMhZfCAyPOjGwDhfvlxx1KdwSFlyC/VWz4YD===; UserName=weixin_48246845; UserInfo=b250c3ca7ff445e8a70b7d74707f3f1a; UserToken=b250c3ca7ff445e8a70b7d74707f3f1a; UserNick=weixin_48246845; AU=595; UN=weixin_48246845; BT=1655194228139; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22weixin_48246845%22%2C%22scope%22%3A1%7D%7D; c_dl_prid=-; c_dl_rid=1655194237210_755217; c_dl_fref=https://blog.csdn.net/weixin_48246845; c_dl_fpage=/download/weixin_48246845/84398686; c_dl_um=-; c_page_id=default; log_Id_click=9; c_pref=default; c_ref=default; c_first_page=https%3A//mp.csdn.net/mp_blog/analysis/article/all; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1655194530; log_Id_view=8; dc_tos=rdgk9u; log_Id_pv=8",
                                
        }
        response = requests.get(url=self.url,headers=headers)
        #response.encoding="utf-8"
        html = response.json
        
        print(html)

        pares_html = etree.HTML(html)
        wenzhuang = pares_html.xpath('//*[@id="data-analy"]/div[2]/div/div[1]/div/p[2]/text()')
        print(wenzhuang)

        yundu=pares_html.xpath('//*[@id="data-analy"]/div[2]/div/div[5]/div/p[2]/text()')
        print(yundu)

if __name__=="__main__":
    CSDNSpider().get_data()




