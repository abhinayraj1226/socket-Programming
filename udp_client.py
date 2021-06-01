import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 12342

msg = "Hello, from udp "

sock.sendto(msg.encode(),(host, port))