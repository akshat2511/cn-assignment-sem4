import socket
HOST = '127.0.0.1'
PORT = 4562
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = input("Enter message: ")
        s.sendto(message.encode(),(HOST, PORT))
        print('Message sent!')
        akshat,addr=s.recvfrom(1024)
        print(akshat.decode())