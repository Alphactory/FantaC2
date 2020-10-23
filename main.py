import socket
import threading
from ClientObject import ClientObject
import time
import subprocess

port = 9998
host = ""


# limit ip, blank means anything


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))

    server_sock.listen()

    print("Server is listening")
    while True:
        (client_sock, addr) = server_sock.accept()
        # blocking method
        thread = threading.Thread(target=ClientObject, args=(client_sock,))
        thread.start()


main()
