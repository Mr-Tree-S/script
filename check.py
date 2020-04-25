from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.settimeout(1)
s.connect(('ip',6379))
s.send('GET 1\r\n')
data = s.recv(20)
s.close()
if '-NOAUTH' in data:
    return False
else:
    return True
