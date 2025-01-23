# This script was intended to be used with tcp_server.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("0.0.0.0", 9998))
client.send(b"ABCABCABC")
response = client.recv(1024)

print(response.decode())
