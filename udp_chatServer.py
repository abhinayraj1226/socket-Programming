import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #for udp

udp_host = socket.gethostname()
udp_port = 12342

sock.bind((udp_host, udp_port))

sender_name, addr = sock.recvfrom(1024)
print(sender_name.decode()," has connected to the chatRoom\n ctrl+c to exit the chatRoom:")

your_name = input("Enter your name: ").replace('b', '').encode('utf-8')
sock.sendto(your_name,addr)

while True:
    msg = input("Me: ").replace('b', '').encode('utf-8')
    sock.sendto(msg, addr)
    msg = sock.recvfrom(1024)
    print(sender_name.decode(),":", msg[0].decode())
sock.close()
