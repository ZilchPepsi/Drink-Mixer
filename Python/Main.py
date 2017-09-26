import IO
import Network
import time
import Machine


#MAIN LOOP
io = IO.IO()
network = Network.Network()
active = True
startupString = '';
machine = Machine.Machine()


#load file
pin,drinks,mixes, activeDrinks = io.readFile()  #drinks is array of Drink, mixes is
                                                #array of Mix, activeDrinks is array of Drink

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
for x in range(6):
    if activeDrinks[x] is not None:
        startupString += activeDrinks[x].name+':'
    else:
        startupString += "None:"

try:
    while active:
        #check network input
        fromNetwork = network.getReceived()
        if len(fromNetwork) > 0 :
            for x in range(len(fromNetwork)):
                key = int(fromNetwork[x][0])
                if key == Network.HELLO:
                    print("Got a hello")
                    network.addMessage(startupString);
                elif key == Network.MAKE_MIX:
                    print("Got a make mix: {}".format(mixes[int(fromNetwork[x][1])].name))
                elif key == Network.GET_DRINKS:
                    ret = ''
                    ret+= str(len(drinks))+':'
                    for i in range(len(drinks)):
                        ret += drinks[i].name+':'+str(drinks[i].alcoholic)+':'
                    network.addMessage(ret)
                        
                else:
                    print("got {}".format(int(fromNetwork[x][0])))
        else:
            time.sleep(1)
        #check machine input
except KeyboardInterrupt:
    print("Shutting down")
    network.shutdown()
    io.writeFile(pin,drinks,mixes,activeDrinks)
    io.closeFile()

    


























                   
