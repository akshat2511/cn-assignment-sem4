import socket
hostname = '127.0.0.1'
serverport=12000
serversocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
m=input('enter any message')
serversocket.sendto(m.encode(),(hostname,serverport))
newm,serveraddr=serversocket.recvfrom(1024)
print(newm.decode())
serversocket.close()