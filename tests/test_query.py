# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 16:14
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : test_logistics
# @Software: PyCharm

import  unittest
from base.method import Method
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

'''销售管理模块所有查询'''
class XSGL(unittest.TestCase):
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

	# def test_001_016(self):
	#
	# 	for i in range(1,16):
	# 		r = self.obj.get(row=i)
	# 		# print(r.text)
	# 		self.isContent(r=r,row=i)
	# 		self.excel.writeResult(i,'pass')

	def test_001(self):
		u"促销政策查询"
		r = self.obj.get(row=1)
		# print(r.text)
		self.isContent(r=r,row=1)
		self.excel.writeResult(1,'pass')

	def test_002(self):
		u"销售价格管理查询"
		r = self.obj.get(row=2)
		# print(r.text)
		self.isContent(r=r,row=2)
		self.excel.writeResult(2,"pass")

	def test_003(self):
		u"销售订单查询"
		r = self.obj.get(row=3)
		# print(r.text)
		self.isContent(r=r,row=3)
		self.excel.writeResult(3,"pass")

	def test_004(self):
		u"销售订单列表查询"
		r = self.obj.get(row=4)
		# print(r.text)
		self.isContent(r=r,row=4)
		self.excel.writeResult(4,"pass")

	def test_005(self):
		u"销售出库查询"
		r = self.obj.get(row=5)
		# print(r.text)
		self.isContent(r=r,row=5)
		self.excel.writeResult(5,"pass")

	def test_006(self):
		u"销售出库明细表查询"
		r = self.obj.get(row=6)
		# print(r.text)
		self.isContent(r=r,row=6)
		self.excel.writeResult(6,"pass")

	def test_007(self):
		u"销售发货查询"
		r = self.obj.get(row=7)
		# print(r.text)
		self.isContent(r=r,row=7)
		self.excel.writeResult(7,"pass")

	def test_008(self):
		u"销售发货明细表查询"
		r = self.obj.get(row=8)
		# print(r.text)
		self.isContent(r=r,row=8)
		self.excel.writeResult(8,"pass")

	def test_009(self):
		u"销售退货查询"
		r = self.obj.get(row=9)
		# print(r.text)
		self.isContent(r=r,row=9)
		self.excel.writeResult(9,"pass")

	def test_010(self):
		u"销售退货明细表查询"
		r = self.obj.get(row=10)
		# print(r.text)
		self.isContent(r=r,row=10)
		self.excel.writeResult(10,"pass")

	def test_011(self):
		"销售调拨查询"
		r = self.obj.get(row=11)
		# print(r.text)
		self.isContent(r=r,row=11)
		self.excel.writeResult(11,"pass")

	def test_012(self):
		u"客户返利查询"
		r = self.obj.get(row=12)
		# print(r.text)
		self.isContent(r=r,row=12)
		self.excel.writeResult(12,"pass")

	def test_013(self):
		u"客户返利列表查询"
		r = self.obj.get(row=13)
		# print(r.text)
		self.isContent(r=r,row=13)
		self.excel.writeResult(13,"pass")

	def test_014(self):
		u"客户返利明细查询"
		r = self.obj.get(row=14)
		# print(r.text)
		self.isContent(r=r,row=14)
		self.excel.writeResult(14,"pass")

	def test_015(self):
		u"委托代销查询"
		r = self.obj.get(row=15)
		# print(r.text)
		self.isContent(r=r,row=15)
		self.excel.writeResult(15,"pass")

	def test_016(self):
		u"委托代销结算查询"
		r = self.obj.get(row=16)
		# print(r.text)
		self.isContent(r=r,row=16)
		self.excel.writeResult(16,"pass")


