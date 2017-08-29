import IO
import Network


#MAIN LOOP
io = IO.IO()
network = Network.Network()

#load file
pin,drinks,mixes = io.readFile()    #drinks is array of Drink, mixes is
                                    #array of Mix

#start network
network.start()



#send startup data
toSend = ''
toSend +=Network.init+':'
toSend += str(pin)+':'

toSend += str(len(drinks))+':'
for i in range(len(drinks)):
    toSend += drinks[i].name+':'+drinks[i].alocholic+':'

toSend+= str(len(mixes))+':'
for i in range(len(mixes)):
    toSend += mixes[i].name+':'
    toSend += str(len(mixes[i].drinks))+':'
    for j in range(len(mixes[i].drinks)):
        toSend += mixes[i].drinks[j].name+':'

toSend+=toSend.initDone

network.addMessage(toSend.decode("utf-8"))

#check network input
fromNetwork = network.getReceived()
if len(fromNetwork) > 0 :
    for x in range(len(fromNetwork)):
        interpretNetworkAction(fromNetwork(x))
        
#check machine input
    

#clean up
network.shutdown()
io.closeFile()


def interpretNetworkAction(messages):#TODO
    pass
