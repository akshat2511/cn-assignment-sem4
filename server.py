import socket
import random
import time

def checksum(data):
    return sum(data) & 0xffffffff

def send_packet(sock, packet, addr):
    sock.sendto(packet, addr)

def receive_packet(sock, buffer_size):
    return sock.recvfrom(buffer_size)

def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    buffer_size = 1024
    timeout = 2  # in seconds
    max_attempts = 5

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))

    while True:
        data, client_addr = receive_packet(sock, buffer_size)
        seq_num, payload, checksum_rcvd = data.split(b':')

        if checksum(payload) == int(checksum_rcvd):
            ack_packet = f"ACK:{seq_num.decode()}".encode()
            send_packet(sock, ack_packet, client_addr)
            print(f"Acknowledgment sent for sequence number {seq_num.decode()}")
        else:
            print("Checksum error. Packet discarded.")

        attempts = 0
        while attempts < max_attempts:
            try:
                sock.settimeout(timeout)
                data, client_addr = receive_packet(sock, buffer_size)
                seq_num, payload, checksum_rcvd = data.split(b':')

                if checksum(payload) == int(checksum_rcvd):
                    ack_packet = f"ACK:{seq_num.decode()}".encode()
                    send_packet(sock, ack_packet, client_addr)
                    print(f"Acknowledgment sent for sequence number {seq_num.decode()}")
                else:
                    print("Checksum error. Packet discarded.")

                break  # Exit the retry loop if successful 
            except socket.timeout:
                attempts += 1
                print(f"Timeout: Retransmitting packet {seq_num.decode()}")
                send_packet(sock, data, client_addr)

if __name__ == "__main__":
    main()
# bankers algorithm
