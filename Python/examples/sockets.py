import socket
import threading

class thrd(threading.Thread):
    def __init__ (self, state):
        threading.Thread.__init__(self)
        self.state = state
        self.sock = socket.socket()
        self.host = 'localhost'
        self.port = 1234

    def run(self):
        if self.state == 0:
            #server
            self.sock.bind((self.host,self.port))
            self.sock.listen(1)
            c, addr = self.sock.accept()
            print("got connection from", addr)
            c.send(b'thanks for connecting')
            c.close()
            self.sock.close()
        else:
            #client
            self.sock.connect((self.host,self.port))
            data = self.sock.recv(1024)
            print("Recieved", data)
            self.sock.close()




serverThread = thrd(0)
clientThread = thrd(1)

serverThread.start()
clientThread.start()
