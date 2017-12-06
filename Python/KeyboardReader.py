import keyboard
import threading
import Machine

class KeyboardReader:
    running = False

    def __init__(self):
        keyboard.hook_key('left', KeyboardReader.pressedLeft, KeyboardReader.releasedLeft)
        keyboard.hook_key('right', KeyboardReader.pressedRight, KeyboardReader.releasedRight)



    
    def pressedLeft():
        Machine.enabled = True
        if not KeyboardReader.running:
            KeyboardReader.running = True
            Machine.moveLeft_debug(Machine.Machine.maxSpeed)
            
    def releasedLeft():
        Machine.enabled = False
        KeyboardReader.running = False
        
    def pressedRight():
        Machine.enabled = True
        if not KeyboardReader.running:
            KeyboardReader.running = True
            Machine.moveRight_debug(Machine.Machine.maxSpeed)
            
    def releasedRight():
        Machine.enabled = False
        KeyboardReader.running = False

try:
    k = KeyboardReader()

except KeyboardInterrupt:
    keyboard.unhook_all()
    print("done")
