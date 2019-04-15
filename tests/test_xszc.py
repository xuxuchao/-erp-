# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 0009 上午 10:52
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : test_XSZC
# @Software: PyCharm

import  unittest
import  json
from base.method import Method
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson


a = {
	"price_data": [{"company_id":10003,"customer_type_id":0,"customer_id":611,"goods_id":18284,"sale_price":"333","start_time":"2019-04-09"}],
	"sign": "3d9631e6c73b4a3a9747568bea8a08ad"
}
'''销售政策管理'''
class XSZC(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.excel=OperationExcel()
		self.operationJson=OperationJson()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['code'], 200)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.obj.isContent(row=row,str2=r.text))


	def test_017(self):
		u"新增促销政策"
		r =self.obj.post(row=17,data=self.operationJson.getRequestsData(row=17))
		self.isContent(r=r,row=17)
		self.excel.writeResult(17,'pass')


	def test_018(self):
		u"新增销售价格"
		data=self.operationJson.getRequestsData(row=18)
		r=self.obj.post(row=18,data=data)
		self.isContent(r=r,row=18)
		self.excel.writeResult(18,'pass')


	def test_019(self):
		u"新增销售订单"
		data=self.operationJson.getRequestsData(row=19)
		r=self.obj.post(row=19,data=data)
		self.isContent(r=r,row=19)
		self.excel.writeResult(19,'pass')

	def test_020(self):
		u"新增销售出库单（直接新增商品）"
		data=self.operationJson.getRequestsData(row=20)
		r=self.obj.post(row=20,data=data)
		self.isContent(r=r,row=20)
		self.excel.writeResult(20,'pass')

	def test_021(self):
		u"新增销售退货"
		data=self.operationJson.getRequestsData(row=21)
		r=self.obj.post(row=21,data=data)
		self.isContent(r=r,row=21)
		self.excel.writeResult(21,'pass')

	def test_024(self):
		pass