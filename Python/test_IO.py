import IO


io = IO.IO(IO.FILENAME)

pin, drinks, mixes = io.readFile()

for d in drinks:
    print("{}:{}".format(d.name, d.alcoholic))
    
print(pin)
print(len(drinks))
print(len(mixes))

io.writeFile(pin,drinks,mixes)

io.closeFile()
