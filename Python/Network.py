import socket
import threading
import array

#########################
# Globals
#########################
TIMEOUT = 10

#########################
# BITMASKS
#########################
makeMix = 0
addMix = 1
modifyMix = 2
deleteMix = 3

addDrink = 4
deleteDrink = 5

init = 6
initDone = 7

Hello = 8
Goodbye = 9

class Network(threading.Thread):

    def __init__(self, port = 1234):
        threading.Thread.__init__(self)
        
        self.toSend = []
        self.received = []

        self.sendLock = threading.Lock()
        self.receivedLock = threading.Lock()
        
        self.sock = socket.socket()
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
                    c.send(self.toSend.pop(0).encode('utf-8'))
        self.sendLock.release()
            
    def run(self):
        self.active = True
        self.sock.bind((self.host,self.port))
        self.sock.listen(1)
        c, addr = self.sock.accept()
        c.settimeout(TIMEOUT)

        #main loop
        while self.active:
            data = b''
            try:
                data = c.recv(1024)#TODO shouldn't just grab 1024
            except socket.timeout:
                pass
            if data != b'':
                #do stuff here with data received
                self.received.append(data.strip().decode('utf-8'))
            if len(self.toSend) !=0:
                self.sendMessages(c)
    
            
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
