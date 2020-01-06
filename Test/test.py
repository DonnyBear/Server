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
	global buff, CNT
	with open("produce.txt", "w") as f:
		while CNT < 50000:
			num = CNT
			CNT += 1
			result = buff.push(num)
			if not result:
				CNT -= 1
				time.sleep(0.001)
				continue
			f.write(str(num) + "\t" + str(buff.buff[(buff.write_fence + buff.max_size - 1)%buff.max_size]) + "\n")

def comsumer():
	global buff, comsume_data, comsume_num, CNT
	read_cnt = 0
	with open("comsumer.txt", "w") as f:
		while read_cnt < 50000:
			result = buff.pop()
			if result is None:
				time.sleep(0.001)
				print "pop None", read_cnt
				continue
			read_cnt += 1
			f.write(str(result) + "\n")

if __name__ == "__main__":
	produce_data = []
	comsume_num = 0
	comsume_data = []
	CNT = 0
	buff = CycleBuff.CycleBuff(50)
	a = threading.Thread(target=producer)
	b = threading.Thread(target=comsumer)
	a.start()
	b.start()