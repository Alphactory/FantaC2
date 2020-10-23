import threading
import sys


class ClientObject:
    def __init__(self, client_sock, clientin=None, clientout=None, clienterr=None):
        self.client_sock = client_sock
        self.threads = []
        self.clientin = clientin
        self.clientout = clientout
        self.clienterr = clienterr
        self.handle(self.client_sock)

    def handle(self, client_sock):
        recvthread = threading.Thread(target=self.handlesend, args=(client_sock,))
        sendthread = threading.Thread(target=self.handlerecv, args=(client_sock,))
        self.threads.append(recvthread)
        self.threads.append(sendthread)
        print(self.threads)
        for thread in self.threads:
            thread.start()

    def handlesend(self, client_sock):
        try:
            while True:
                self.client_sock.send(input().encode())
        except ConnectionAbortedError or ConnectionResetError:
            print("Could not connect to host")

    def handlerecv(self, client_sock):
        try:
            while True:
                print(self.client_sock.recv(1024).decode(), end="")
        except ConnectionAbortedError or ConnectionResetError:
            print("Client has closed connection")
