import socket
servername='127.0.0.1'
serverport=12000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sentence=input("enter ")
serversocket.sendto(sentence.encode(),(servername,serverport))
new,serveradress=serversocket.recvfrom(1024)
print(new.decode())
serversocket.close()

