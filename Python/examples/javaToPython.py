import socket


alive = True
sock = socket.socket()

sock.bind(('localHost', 1234))
sock.listen(1)
c, addr = sock.accept()
print("got connection from", addr)
c.settimeout(3)
c.send('thanks for connecting'.encode("utf-8"))
try:
    data = c.recv(1024);
except socket.timeout:
    print("I timed out")
    data = b'OOPS NO'
    
print(data.decode("utf-8"))
c.close()
sock.close()
