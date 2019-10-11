__author__ = 'Administrator'

from Network.NetworkBuff import NetworkBuff

BUFF_SIZE = 5*1024

class NetworkSocket(object):
    def __init__(self, socket, addr):
        self.socket = socket
        self.addr = addr
        self.buff = NetworkBuff.NetworkBuff()

    def read(self):
        return self.buff.read()

    def write(self, msg):
        return self.buff.write(msg)

    def send(self, msg):
        pass
