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
        print("length", self.msg_data[:2])
        num = int.from_bytes(self.msg_data[:2],byteorder='big') + 2
        if len(self.msg_data) < num:
            return None
        data = self.msg_data[2:num]
        self.msg_data = self.msg_data[num:]
        return data
        # try:
        #     if msg_length > num:
        #         data = self.arr_msg[0][:num]
        #         self.can_read -= num
        #         self.arr_msg[0] = self.arr_msg[0][num:]
        #     elif msg_length == num:
        #         data = self.arr_msg.pop(0)
        #         self.can_read -= num
        #     else:
        #         left_num = num - msg_length
        #         data = self.arr_msg.pop(0)
        #         data = data + self.read(left_num)
        # except:
        #     print("GE_EXC,socket读取流失败")
        # return data

    def write(self, msg):
        if self.msg_data and len(self.msg_data) >= MAX_LENGTH:
            print("GE_EXC,msg too long")
            return False
        if not self.msg_data:
            self.msg_data = msg
        else:
            self.msg_data += msg
        return True
