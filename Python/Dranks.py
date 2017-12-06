
class Drink:
    drinkList = []
    def __init__(self, name, alcoholic):
        self.name = name
        self.alcoholic = alcoholic
        Drink.drinkList.append(self)

    #class function
    #O(N)
    def hasDrink(name):
        for i in range(len(Drink.drinkList)):
            if Drink.drinkList[i].name == name:
                return True
        return False

    #class function
    #O(N)
    def getDrink(name):
        for i in range(len(Drink.drinkList)):
            if Drink.drinkList[i].name == name:
                return Drink.drinkList[i]

class Mix:
    def __init__(self, name):
        self.name = name    #the name of the mix
        self.drinks = []    #tuples of the drink and how many shots (drink,shots)
        
    def addDrink(self, drink, shot):
        self.drinks.append((drink,shot))

    
        
