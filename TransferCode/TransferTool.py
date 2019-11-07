#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# XRLAM("TransferTool")
#===============================================================================
# 注释
#===============================================================================


class TransferTool(object):

	def __init__(self):
		self.match_words = [
			["public var", "public"],
			["private var", "private"],
			[":int", ":number"],
			[":Number", ":number"],
			[":Boolean", ":boolean"],
			[":String", ":string"],
			[":Array;", ":Array<any>;"],
			["Vector.", "Array"],
			[" function ", " "],
			[":*", ":any"],
			["GameString.format", "GameString.instance.format"],
			["ConfigMgr.get_config_as_arr", "ConfigMgr.instance.get_config_as_arr"],
			["TimeMgr.unreg_logic_frame_30", "TimeMgr.instance.unreg_logic_frame_30"],
			["\toverride ", ""],
			["public static var", "public static"],
			[":Point", ":egret.Point"],
			[": int", ":number"],
			[": Number", ":number"],
			[": String", ":string"],
			[": Boolean", ":boolean"],
			[": Array", ":Array<any>"],
			[": *", ":any"],
			[": Point", ":egret.Point"],
			["MouseEvent.MOUSE_OUT", "mouse.MouseEvent.ROLL_OUT"],
			["MouseEvent.MOUSE_OVER", "mouse.MouseEvent.ROLL_OUT"],
			[":INotication", "GameNotification"],
			[".mouseEnabled", ".touchEnabled"],
			["TimeMgr.unreg_second", "TimeMgr.instance.unreg_second"],
			["TimeMgr.reg_second", "TimeMgr.instance.reg_second"],
		]
		self.variable = set()
		self.function = set()
		self.txt = []

	def setTxt(self, source):
		self.txt = source

	def search(self):
		self.variable = set()
		self.function = set()
		self.function.add("getImgItem")
		self.function.add("getImage")
		self.function.add("getButton")
		self.function.add("getContain")
		self.function.add("getTileList")
		self.function.add("getList")
		self.function.add("getPage")
		self.function.add("getScrollBar")
		self.function.add("getTab")
		self.function.add("getItemRender")
		self.function.add("getText")
		self.function.add("getToggleButton")
		self.function.add("getImgItem")
		self.function.add("getControl")
		self.function.add("getGShape")
		self.function.add("getGProgressBar")
		self.function.add("getSlide")
		self.function.add("getComboBox")
		self.function.add("getRichInputTxt")
		self.function.add("getHGroup")
		self.function.add("getVGroup")
		self.function.add("getGSwitch")
		self.function.add("loadFromXml")

		while not self.txt[0].startswith("\tpublic"):
			self.txt.pop(0)
		self.txt.pop()
		# 查找变量
		match_word1 = "public var "
		match_word1_len = len(match_word1)
		match_word2 = "private var "
		match_word2_len = len(match_word2)
		colon_match = " :"
		colon = ":"
		for index, text in enumerate(self.txt):
			# 有的人喜欢在冒号前加空格，去除，方便匹配
			text = text.replace(colon_match, colon)
			self.txt[index] = text
			index = text.find(match_word1)
			cur_index = match_word1_len
			if index < 0:
				index = text.find(match_word2)
				cur_index = match_word2_len
			if index < 0:
				continue
			index += cur_index
			end_index = text[index:].find(colon)
			if end_index < 0:
				print "匹配到了变量前缀，却匹配不到空格，找不到变量"
				continue
			end_index += index
			self.variable.add(text[index:end_index])
		# 查找函数
		match_word = "function "
		match_word_len = len(match_word)
		open_brace = "("
		for text in self.txt:
			index = text.find(match_word)
			if index < 0:
				continue
			index += match_word_len
			end_index = text.find(open_brace)
			if end_index < 0:
				print "匹配到了函数前缀，却匹配不到左括号，找不到函数名"
				continue
			self.function.add(text[index:end_index])
		# 查找临时变量， 将其从变量中去除，人工自行修改
		var_word = "\tvar "
		equal_word = "="
		comma_word = ","
		for text in self.txt:
			index = text.find(var_word)
			if index < 0:
				continue
			end_index = text.find(equal_word)
			txt_var = text[index+len(var_word):end_index]
			txt_var = txt_var.strip()
			arr_var = txt_var.split(comma_word)
			for var in arr_var:
				self.variable.discard(var.strip())
				self.function.discard(var.strip())



	def replace(self):
		for index, text in enumerate(self.txt):
			for key, val in self.match_words:
				text = text.replace(key, val)
			self.txt[index] = text

	# 增加this
	def addPoint(self):
		match_word = ["\t", ",", "(", "= ", "return "]
		add_word = "this."
		for t_index, text in enumerate(self.txt):
			for word in match_word:
				for var in self.variable:
					match = "%s%s" % (word, var)
					index = text.find(match)
					if index < 0:
						continue
					index += len(word)
					self.txt[t_index] = "%s%s%s" % (text[:index], add_word, text[index:])
		for t_index, text in enumerate(self.txt):
			for word in match_word:
				for var in self.function:
					match = "%s%s" % (word, var)
					index = text.find(match)
					if index < 0:
						continue
					index += len(word)
					self.txt[t_index] = "%s%s%s" % (text[:index], add_word, text[index:])


