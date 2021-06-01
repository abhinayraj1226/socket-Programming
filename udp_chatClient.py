import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 12342

your_name = input("Enter your name: ").replace('b', '').encode('utf-8')

sock.sendto(your_name,(host, port))

sender_name, addr = sock.recvfrom(1024)
print(sender_name.decode(), " has connected to the chatRoom \n Press ctrl+c to exit the chatRoom\n")

while True:
    msg = sock.recvfrom(1024)
    print(sender_name.decode(),":", msg[0].decode())
    msg = input("Me: ").replace('b', '').encode('utf-8')
    sock.sendto(msg, addr)

sock.close()
