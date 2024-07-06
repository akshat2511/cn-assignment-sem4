# write a udp client python to code to reverse a string
import socket
HOST = '127.0.0.1'
PORT = 4562
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Server listening on', (HOST, PORT))
        data ,addr = s.recvfrom(1024)
        print('Received:', data.decode())
        str = data.decode()
        reversed_str = str[::-1]    
        s.sendto(reversed_str.encode(), addr)
