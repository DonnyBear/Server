#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# XRLAM("test")
#===============================================================================
# 注释
#===============================================================================
import time
import random
import threading
from CycleBuff import CycleBuff

def producer():
	global buff, produce_num, produce_data, CNT
	while produce_num < 500000:
		num = CNT
		CNT += 1
		produce_data.append(num)
		produce_num += 1
		result = buff.push(num)
		if not result:
			produce_num -= 1
			produce_data.pop()
			time.sleep(0.001)
			continue

def comsumer():
	global buff, comsume_num, produce_num, comsume_data, a
	while comsume_num < 500000:
		# print buff.read_fence, buff.buff[buff.read_fence - 2:]
		result = buff.pop()
		if result is None:
			time.sleep(0.001)
			continue
		print result
		comsume_data.append(result)
		comsume_num += 1
		if produce_num < comsume_num:
			# print "error", buff.read_fence, buff.buff[buff.read_fence - 2:]
			with open("test.txt", "w") as f:
				for i in xrange(comsume_num):
					f.write(str(produce_data[i]) + "\t" + str(comsume_data[i]) + "\n")
				f.close()
			break
		if result != produce_data[comsume_num-1]:
			# print "data error", result
			with open("test.txt", "w") as f:
				for i in xrange(comsume_num):
					f.write(str(produce_data[i]) + "\t" + str(comsume_data[i]) + "\n")
				f.close()
			break

if __name__ == "__main__":
	produce_num = 0
	produce_data = []
	comsume_num = 0
	comsume_data = []
	CNT = 0
	buff = CycleBuff.CycleBuff(500)
	a = threading.Thread(target=producer)
	b = threading.Thread(target=comsumer)
	a.start()
	b.start()