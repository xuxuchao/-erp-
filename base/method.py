# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 上午 9:06
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : method
# @Software: PyCharm

import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

operationExcel=OperationExcel()

class Method:
	def __init__(self):
		self.operationJson=OperationJson()
		self.excel=OperationExcel()

	def post(self,row,data):
		try:
			r=requests.post(
				url=self.excel.getUrl(row=row),
				data=data,
				headers=getHeadersValue(),
				timeout=6
			)
			return r
		except Exception as e:
			raise RuntimeError("接口请求发生未知的错误")

	def get(self,row):
		r=requests.get(
			url=self.excel.getUrl(row=row),
			params={"sign":"c0a75f6168f41d815786a6d1e86b22ab"},
			headers=getHeadersValue(),
			timeout=6
		)
		return r

	def isContent(self,row,str2):
		flag=None
		if self.excel.getExpect(row=row) in str2:
			flag=True
		else:
			flag=False
		return flag
