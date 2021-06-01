import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #for udp

udp_host = socket.gethostname()
udp_port = 12342

sock.bind((udp_host, udp_port))

data, addr = sock.recvfrom(1024)
print("Client:", data.decode(), "\nAddress Details : ", addr)
# sock.sendto(msg1,addr)
currTime = time.ctime(time.time())
sock.sendto(currTime.replace('b', '').encode('utf-8'), addr)
sock.close()
