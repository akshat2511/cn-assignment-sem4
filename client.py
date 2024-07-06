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

    seq_num = 0
    while True:
        payload = f"Data Packet {seq_num}".encode()
        checksum_val = checksum(payload)
        packet = f"{seq_num}:{payload.decode()}:{checksum_val}".encode()

        send_packet(sock, packet, (server_ip, server_port))
        print(f"Sent packet with sequence number {seq_num}")

        try:
            sock.settimeout(timeout)
            data, addr = receive_packet(sock, buffer_size)
            if data.decode().startswith("ACK"):
                ack_seq_num = data.decode().split(":")[1]
                print(f"Received acknowledgment for sequence number {ack_seq_num}")
                seq_num += 1
        except socket.timeout:
            print("Timeout: Retransmitting packet")
            seq_num -= 1  # Retransmit the same packet
            if seq_num < 0:
                seq_num = 0

        time.sleep(1)  # Add a delay between packet transmissions

if __name__ == "__main__":
    main()
