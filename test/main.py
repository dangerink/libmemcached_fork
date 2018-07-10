import socket
import time
from pylibmc.test import make_test_client
import pylibmc

class PyLibMCWrapper(object):
    def __init__(self, host, port):
        self.custom_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.custom_socket.connect((host, port))
        self.cl = make_test_client(binary=True)
        self.custom_socket.send(b"test\r\n")
        resp = self.custom_socket.recv(4096)
        print(resp)


mc = pylibmc.Client(["135.29.51.2"], binary=True)
mc.behaviors['ketama'] = True
mc.behaviors['remove_failed'] = 1
mc.behaviors['retry_timeout'] = 2
mc.behaviors['dead_timeout'] = 20
mc.behaviors['connect_timeout'] = 22
#mc.behaviors['auto_eject'] = 0
#time.sleep(10)
print(mc.get_behaviors())
print("enough")
time.sleep(2)
mc.set('1', b'agagag')
mc.set('3', b'agdddagag')
print(mc.get("1"))