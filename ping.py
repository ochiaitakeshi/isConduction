# coding: utf-8
import sys
import socket
#import time

def isConduction(ip):
  sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
  sock.sendto('\x08\x00\xf5\xfc\x01\x01\x01\x02', (ip, 0))

  sock.settimeout(1)
  try:
    data = sock.recv(255)
  except socket.timeout:
    return False
  return True

if __name__ == '__main__':
  ret = isConduction(sys.argv[1])
  if ret:
    print('sotsuu OK')
  else:
    print('sotsuu NG')
