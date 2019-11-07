#!/usr/bin/env python
# -*- coding:UTF-8 -*-

__author__ = 'Administrator'

MAX_LENGTH = 50*1024

class NetworkBuff(object):

	def __init__(self):
		self.msg_data = None

	def read(self):
		if not self.msg_data:
			return None
		num = int.from_bytes(self.msg_data[:2], byteorder='big') + 2
		print("length", num)
		if len(self.msg_data) < num:
			return None
		data = self.msg_data[2:num]
		self.msg_data = self.msg_data[num:]
		print(data)
		return data

	def write(self, msg):
		if self.msg_data and len(self.msg_data) >= MAX_LENGTH:
			print("GE_EXC,msg too long")
			return False
		if not self.msg_data:
			self.msg_data = msg
		else:
			self.msg_data += msg
		return True
