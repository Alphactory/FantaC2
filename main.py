import socket
import threading
import time

port = 9998
host = ""


# limit ip, blank means anything

def handle(client_sock):
    recvthread = threading.Thread(target=handlesend, args=(client_sock,))
    sendthread = threading.Thread(target=handlerecv, args=(client_sock,))
    sendthread.start()
    recvthread.start()


def handlesend(client_sock):
    while True:
        client_sock.send(input(">").encode())

def handlerecv(client_sock):
    try:
        while True:
            print(client_sock.recv(1024).decode(), end="")
    except ConnectionAbortedError:
        print("Client has closed connection")


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))

    server_sock.listen()

    print("Server is listening")
    while True:
        (client_sock, addr) = server_sock.accept()
        # blocking method
        thread = threading.Thread(target=handle, args=(client_sock,))
        thread.start()


main()
