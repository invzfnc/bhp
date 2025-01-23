# A simple TCP client

import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - use standard IPv4 address or hostname
# SOCK_STREAM - this will be a TCP client

# connect the client to the server
client.connect((target_host, target_port))

# send some data as bytes
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
