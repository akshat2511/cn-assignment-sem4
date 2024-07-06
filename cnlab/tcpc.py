import socket
hostname='127.0.0.1'
severport=12000

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((hostname,severport))

sentence=input("enter ")

serversocket.send(sentence.encode())
n=serversocket.recv(1024)

print(n.decode())
serversocket.close()