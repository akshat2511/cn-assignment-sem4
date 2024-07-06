import socket
serverport=12000
cliensocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliensocket.bind(('',serverport))
cliensocket.listen(1)
print("send")
while True:
    connection_socket,addr= cliensocket.accept()
    m=connection_socket.recv(1024).decode().upper()
    connection_socket.send(m.encode())
   