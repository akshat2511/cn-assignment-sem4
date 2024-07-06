import socket

server_name = '127.0.0.1'  
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = input("Input lowercase sentence: ")
client_socket.send(sentence.encode())

modified_sentence = client_socket.recv(1024).decode()
print('From Server:', modified_sentence)

client_socket.close()
