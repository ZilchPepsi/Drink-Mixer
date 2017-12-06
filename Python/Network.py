##TODO#########################
## when connection is dropped, set a signal somewhere
###############################


import socket
import threading

#########################
# Globals
#########################
TIMEOUT = 2
SERVER_TIMEOUT = 5

#########################
# BITMASKS
#########################
MAKE_MIX = 0
ADD_MIX = 1
MODIFY_MIX = 2
DELETE_MIX = 3

GET_DRINKS = 11
ADD_DRINK = 4
DELETE_DRINK = 5

#machine info
GET_ACTIVE_DRINKS = 12
SET_ACTIVE_DRINKS = 13

INIT = 6
INIT_CONFIRM = 8 # not used

HELLO = 9
GOODBYE = 10

class Network(threading.Thread):

    def __init__(self, port = 1234):
        threading.Thread.__init__(self)
        
        self.toSend = []
        self.received = []

        self.sendLock = threading.Lock()
        self.receivedLock = threading.Lock()
        
        self.host = ''
        self.port = port
        self.active = False
        
    #gets the port being used        
    def getPort(self):
        return self.port

    #sets the port to use, only if the server is not running
    def setPort(self, port):
        if not self.active:
            self.port = port

    #INTERNAL - sends the messages queued to be sent
    def sendMessages(self,c):
        self.sendLock.acquire()
        length = len(self.toSend)
        for _ in range(length):
            try:
                print("Sending {}".format(self.toSend[0]))
                c.send(self.toSend.pop(0).encode('utf-8'))
            except ConnectionResetError:
                self.sendLock.release()
                raise
        self.sendLock.release()


    #INTERNAL       
    def run(self):
        print("starting network thread")
        self.active = True
        
        c, addr = self.waitForConnect()
        #main loop
        while self.active:
            data = b''
            timeout = False
            try:
                timeout = False
                data = c.recv(32)
            except socket.timeout:
                timeout = True
            except ConnectionResetError:
                c.shutdown(socket.SHUT_RDWR)
                c.close()
                c, addr = self.waitForConnect()
                if c is None:
                    break
                print("got a ConnectionResetError")
            if data != b'':
                self.receivedLock.acquire()
                self.received.append(data)
                self.receivedLock.release()
            elif not timeout:
                c.shutdown(socket.SHUT_RDWR)
                c.close()
                c, addr = self.waitForConnect()
                if c is None:
                    break
            if len(self.toSend) !=0:
                try:
                    self.sendMessages(c)
                except ConnectionResetError:
                    c.shutdown(socket.SHUT_RDWR)
                    c.close()
                    c, addr = waitForConnect()
                    if c is None:
                        break
        if c is not None:
            c.shutdown(socket.SHUT_RDWR)
            c.close()


    #INTERNAL 
    def waitForConnect(self):
        print("setting up a connection...")
        self.sock = socket.socket()
        self.sock.bind((self.host,self.port))
        self.sock.listen(1)
        self.sock.settimeout(SERVER_TIMEOUT)
        while self.active:
            try:
                c, addr = self.sock.accept()
                break
            except socket.timeout:
                pass
        if not self.active:
            return (None, None)
        else:
            c.settimeout(TIMEOUT)
            self.sock.close()
            print("Got one")
            return (c, addr)
    
    def shutdown(self):
        self.active = False

    #returns the list of messages received        
    def getReceived(self):
        self.receivedLock.acquire()
        returning = list(self.received)
        del self.received[:]
        self.receivedLock.release()
        return returning
        
    #adds a messsage to be sent
    def addMessage(self, message):
        self.sendLock.acquire()
        self.toSend.append(message)
        self.sendLock.release()
