import socket

host = socket.gethostname()

port = 12344

s = socket.socket()
s.connect((host, port))
s.sendall('Welcome, user!'.encode())
data = s.recv(1024)
s.close()
print(repr(data))