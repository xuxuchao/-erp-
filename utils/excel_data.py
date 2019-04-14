# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 上午 9:31
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : excel_data
# @Software: PyCharm

from base.get_Token import Get_Token

class ExcelVariable:
	caseID=0
	Title=1
	url=2
	request_data=3
	expect=4
	result=5

def getCaseID():
	return ExcelVariable.caseID

def getTitle():
	return ExcelVariable.Title

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers={
		"Token":Get_Token(),
		"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
		"Referer":"http://testerp.taijierp.cn/"
	}
	return headers


