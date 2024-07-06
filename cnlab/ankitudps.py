import socket
serverport = 12000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('', serverport))
print("ready")
while True:
    message, clientaddress = serversocket.recvfrom(1024)
    new_message = message.decode().upper()
    serversocket.sendto(new_message.encode(), clientaddress)
