import os.path as OS
import Dranks

FILENAME = "drinks.dat"

class IO:

    def __init__(self, fileName = FILENAME):
        self.FILE = open(fileName, "a+")

    def closeFile(self):
        self.FILE.close()

    #INTERNAL
    def convertBool(var):
        if var == "True":
            return True
        return False

    def readFile(self):
        self.FILE.seek(0)
        pin = int(self.FILE.readline())

        drinkCount = int(self.FILE.readline())
        #drinks = []
        for i in range(drinkCount):
            d = self.FILE.readline().split(':')
            #drinks.append(Dranks.Drink(d[0], IO.convertBool(d[1][:-1])))
            Dranks.Drink(d[0], IO.convertBool(d[1][:-1])) # don't need to save this because it is saved in Dranks.Drink.drinkList
        mixCount = int(self.FILE.readline())
        
        mixes = []
        for i in range(mixCount):
            m = self.FILE.readline().split(':')
            mix = Dranks.Mix(m[0])
            for j in range(2, (int(m[1])*2)+2, 2):
                if Dranks.Drink.hasDrink(m[j]):
                    mix.addDrink(Dranks.Drink.getDrink(m[j]), int(m[j+1]))
                else:
                    print("no such drink {}".format(m[j]))
            mixes.append(mix)
            
        activeDrinks = []
        for i in range(6):
            d = self.FILE.readline()
            if d == '\n' or d == '':
                activeDrinks.append(None)
            elif Dranks.Drink.hasDrink(d):
                activeDrinks.append(Dranks.Drink.getDrink(d))
            else:
                print("No such drink {}, not adding to active drinks".format(d))
            
        
        return (pin, Dranks.Drink.drinkList, mixes, activeDrinks)

    def writeFile(self, pin, drinks, mixes,activeDrinks):
        self.FILE.seek(0)
        self.FILE.truncate()
        self.FILE.write(str(pin)+'\n')
        self.FILE.write(str(len(drinks))+'\n')
        for d in drinks:
            self.FILE.write(d.name+':'+str(d.alcoholic)+'\n')
        self.FILE.write(str(len(mixes))+'\n')
        for m in mixes:
            self.FILE.write(m.name+':'+str(len(m.drinks))+':')
            for i in range(len(m.drinks)):
                d,s = m.drinks[i]
                self.FILE.write(d.name+':'+str(s))
                if i != len(m.drinks)-1:
                    self.FILE.write(':')
            self.FILE.write('\n')
        for ad in activeDrinks:
            if ad is not None:
                self.FILE.write(ad.name+'\n')
            else:
                self.FILE.write('\n')




        
