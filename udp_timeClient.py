import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 12342

msg = "Request time from Server"

sock.sendto(msg.replace('b', '').encode('utf-8'),(host, port))

tm, addr = sock.recvfrom(1024)
print("curr Time from server: ", tm.decode())
# sock.sendto(msg.encode(),(host, port))