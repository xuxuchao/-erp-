# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 16:16
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : get_Token
# @Software: PyCharm


import requests
import json
def Get_Token():
	r=requests.post(
		url="http://glterp.taijierp.cn/system/user/login",
		data={"username":"xuhongchao",
		      "password":"123456",
		      "client_type":1,
		      "sign":"0752ae360b6743e473212792fecb7473"},
		headers={
			"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
			"Referer":"http://testerp.taijierp.cn/",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
		}
	)
	js=json.loads(r.text)
	return js["data"]["token"]
