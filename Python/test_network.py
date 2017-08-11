from Network import Network


net = Network()
net.start()
inpt = ""

while(inpt != "quit"):
    inpt = input(">>")
    net.addMessage(inpt)
    messages = net.getReceived()
    for m in messages:
        print(m)

net.shutdown()
