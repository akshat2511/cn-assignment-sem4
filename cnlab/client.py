import socket
import random
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_packet(seq_num, data):
    packet = f"{seq_num}:{data}".encode()
    sock.sendto(packet, (UDP_IP, UDP_PORT))
    print(f"Sent packet {seq_num}")

def receive_packet():
    data, addr = sock.recvfrom(1024)
    return data.decode().split(':')

def reliable_send(data):
    seq_num = 0
    while True:
        send_packet(seq_num, data)
        try:
            ack_num, _ = receive_packet()
            if int(ack_num) == seq_num:
                seq_num = 1 - seq_num
        except socket.timeout:
            print(f"Timeout for packet {seq_num}, resending...")

# Simulate packet loss
def send_with_loss(data, loss_prob):
    if random.random() > loss_prob:
        reliable_send(data)
    else:
        print("Packet lost")

sock.settimeout(1.0)
loss_prob = 0.1  # 10% packet loss probability
data = "Hello, world!"
send_with_loss(data, loss_prob)

sock.close()
