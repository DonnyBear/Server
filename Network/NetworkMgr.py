#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import select
from queue import Queue
from Network.NetworkSocket import NetworkSocket

__author__ = 'Administrator'

ADDR = ("127.0.0.1", 7000)
class NetworkMgr(object):

    def __init__(self):
        self.buff_queue = Queue()
        self.sock = None
        self.inputs = []
        self.outputs = []
        self.message_queues = {}
        self.is_run = False
        self.f = None

    def start_listen(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        self.sock.bind(ADDR)
        self.sock.listen(1024)
        self.inputs.append(self.sock)
        self.f = open("text.txt", "w")
        self.is_run = True


    def loop(self):
         readable, writeable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
         for s in readable:
             if s == self.sock:
                connection, client_addr = s.accept()
                connection.setblocking(False)
                self.inputs.append(connection)
                self.message_queues[connection] = NetworkSocket.NetworkSocket(connection, client_addr)
             else:
                data = s.recv(1024)
                if data:
                    if not self.message_queues[s].write(data):
                        print("写入出错")
                    if s not in self.outputs:
                        self.outputs.append(s)
                else:
                    if s in self.outputs:
                        self.outputs.remove(s)
                    self.inputs.remove(s)
                    s.close()
                    self.message_queues.pop(s, None)
                # 尝试读取数据
                data = self.message_queues[s].read()
                if not data:
                    continue
                self.f.write(data.decode("utf-8"))
         for s in exceptional:
            print("GE_EXC,套接字出错")
            if s in self.outputs:
                self.outputs.remove(s)
            self.inputs.remove(s)
            s.close()
            self.end_listen()


    def end_listen(self):
        self.outputs.clear()
        self.message_queues = None
        for s in self.inputs:
            s.close()
        self.inputs.clear()
        self.f.close()
        self.is_run = False









