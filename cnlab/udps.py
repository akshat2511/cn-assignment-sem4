import socket
serverport=12000
clientsocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('',serverport))
print("send the message")
while True:
    m,addr=clientsocket.recvfrom(1024)
    new_message=m.decode().upper()
    clientsocket.sendto(new_message.encode(),addr)
