#!/usr/bin/python
import keyboard
import threading
import Machine

class KeyboardReader():
    running = False

    def __init__(self):
        keyboard.hook_key('left', self.pressedLeft, self.releasedLeft)
        keyboard.hook_key('right', self.pressedRight, self.releasedRight)



    
    def pressedLeft(self):
        print("pressed left")
        Machine.enabled = True
        if not KeyboardReader.running:
            KeyboardReader.running = True
            Machine.moveLeft_debug(Machine.Machine.maxSpeed)
            
    def releasedLeft(self):
        print("released left")
        Machine.enabled = False
        KeyboardReader.running = False
        
    def pressedRight(self):
        print("pressed right")
        Machine.enabled = True
        if not KeyboardReader.running:
            KeyboardReader.running = True
            Machine.moveRight_debug(Machine.Machine.maxSpeed)
            
    def releasedRight(self):
        print("released right")
        Machine.enabled = False
        KeyboardReader.running = False


try:
    mac = Machine.Machine()
    k = KeyboardReader()
    while True:
        pass
except KeyboardInterrupt:
    mac.cleanup()
    print("done")
