import IO
import Network
import time


#MAIN LOOP
io = IO.IO()
network = Network.Network()
active = True
startupString = '';


#load file
pin,drinks,mixes = io.readFile()    #drinks is array of Drink, mixes is
                                    #array of Mix

#start network
network.start()


#send startup data
startupString = ''
startupString +=str(Network.INIT)+':'
startupString += str(pin)+':'

startupString += str(len(drinks))+':'
for i in range(len(drinks)):
    startupString += drinks[i].name+':'+str(drinks[i].alcoholic)+':'

startupString+= str(len(mixes))+':'
for i in range(len(mixes)):
    startupString += mixes[i].name+':'
    startupString += str(len(mixes[i].drinks))+':'
    for j in range(len(mixes[i].drinks)):
        startupString += mixes[i].drinks[j][0].name+':'
        startupString += str(mixes[i].drinks[j][1])+':'


try:
    while active:
        #check network input
        fromNetwork = network.getReceived()
        if len(fromNetwork) > 0 :
            for x in range(len(fromNetwork)):
                if int(fromNetwork[x][0]) == Network.HELLO:
                    print("Got a hello")
                    network.addMessage(startupString);
                elif int(fromNetwork[x][0]) == Network.MAKE_MIX:
                    print("Got a make mix: {}".format(mixes[int(fromNetwork[x][1])].name))
                else:
                    print("got {}".format(int(fromNetwork[x][0])))
        else:
            time.sleep(1)
        #check machine input
except KeyboardInterrupt:
    print("Shutting down")
    network.shutdown()
    io.closeFile()

    


























                   
