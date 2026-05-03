#!/usr/bin/python3
import socket

def send_command(command):
    host = '127.0.0.1'
    port = 7356
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall((command + '\n').encode())
        data = s.recv(1024)
        return data.decode().strip()

if __name__ == "__main__":
    print(f"Current Frequency: {send_command('f')}")
    # print(f"Setting Frequency: {send_command('F 100000000')}")
