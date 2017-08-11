from Dranks import Drink
from Dranks import Mix


d1 = Drink("rum", True)
d2 = Drink("sprite", False)
d3 = Drink("vodka", True)

m = Mix("choco")
m.addDrink(d1, 3)
m.addDrink(d2, 1)
m.addDrink(d3, 5)

drinks, shots = m.getDrinks()

for i in range(len(drinks)):
    print("{0:6s}: {1:2d}".format(drinks[i].name, shots[i]))

for i in range(len(Drink.drinkList)):
    print(Drink.drinkList[i].name)

print(Drink.hasDrink("sprite"))
print(Drink.hasDrink("Coca"))
