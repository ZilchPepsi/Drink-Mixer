import IO
import Network
import time
#import Machine


def sortMix(mix):
    drinksList = list(mix.drinks)
    sodas = []
    retList = []
    for d in drinksList:
        if not d[0].alcoholic:
            sodas.append(d)
            drinksList.remove(d)
    while len(drinksList) >0:
        try:
            curMax = 0
            drinkTuple = drinksList[0]
            for i in drinksList:
                index = activeDrinks.index(i[0])
                if index > curMax:
                    curMax = index
                    drinkTuple = i
            retList.append(drinkTuple)
            drinksList.remove(drinkTuple)
        except ValueError:#the drink was not in the list
            print("got value error")
            return []
    for d in sodas:
        retList.append(d)
    return retList


#MAIN LOOP
io = IO.IO()
network = Network.Network()
active = True
startupString = '';


#load file
pin,drinks,mixes, activeDrinks, activeMixers, drinkPositions = io.readFile()
#drinks is array of Drink, mixes is array of Mix, activeDrinks is array of Drink, drinkPostions is array of ints


#initialize machine
#machine = Machine.Machine(dp = drinkPositions)

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
                elif key == Network.MAKE_MIX:#where the magic happens
                    
                    print("Got a make mix: {}".format(mixes[int(fromNetwork[x][1])].name))
                    mix = mixes[int(fromNetwork[x][1])]
                    drinkOrder = sortMix(mix)
                    for d in drinkOrder:
                        print("working on drink {}".format(d[0].name))
                        if d[0].alcoholic:
                            drinkPos = activeDrinks.index(d[0])
                            print("moving to position {}, pouring {} shots".format(drinkPos, d[1]))
                            #machine.moveTrayP(drinkPos)
                            for shot in range(d[1]):
                                print("pouring shot {}".format(shot))
                                 #machine.openAlc(drinkPos)
                            time.sleep(1)
                        else:
                            drinkPos = activeMixers.index(d[0])
                            print("moving to position START, pouring {} shots".format(d[1]))
                            #machine.resetPosition()
                            for shot in range(d[1]):
                            #   machine.openMixer(drinkPos)
                                print("pouring shot {}".format(shot))
                            time.sleep(1)

                    
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
    #machine.cleanup()
    io.writeFile(pin,drinks,mixes,activeDrinks,activeMixers, drinkPositions)
    io.closeFile()


        
        
    


























                   
