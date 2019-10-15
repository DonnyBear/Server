#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# XRLAM("CycleBuff")
#===============================================================================
# 环形缓冲区
#===============================================================================



class CycleBuff(object):

	def __init__(self, max_size):
		self.max_size = max_size
		self.buff = [None] * max_size
		self.left_size = max_size
		self.write_fence = 0
		self.read_fence = 0

	def push(self, num):
		if self.left_size <= 0:
			return False
		self.buff[self.write_fence] = num
		self.write_fence += 1
		self.write_fence = self.write_fence % self.max_size
		self.left_size -= 1
		return True

	def pop(self):
		if self.left_size >= self.max_size:
			return None
		num = self.buff[self.read_fence]
		self.read_fence += 1
		self.read_fence = self.read_fence % self.max_size
		self.left_size += 1
		return num


