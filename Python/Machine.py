#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

'''
BiggerDriver
BCM
pin 2 - enable
pin 3 - direction
pin 4 - pulse

'''


'''
easyDriver
BCM
pin 2 - step
pin 3 - direction
pin 4 - enable
pin 6 - ground
pin 17 - MS1
pin 27 - MS2

process
ENABLE - set LOW
MS1 & 2 - set LOW (for full step)
DIRECTION - set LOW
step - set Low

control
step - low -> high = step
'''


class Machine_BiggerDriver:
    def __init__(self, ad=[None,None,None,None,None,None]):
        self.activeDrinks = ad
        self.pinList = [2,3,4]
        

    def getDrinks(self):
        return self.activeDrinks
    
    def setDrink(self, drink, pos):
        self.activeDrinks[pos] = drink


    def step(self):
        time.sleep(0.0003)
        GPIO.output(self.pinList[2], GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(self.pinList[2], GPIO.LOW)

    def step_control(self, count, maxSpeed, startSpeed = .001):
        #count - number of rotations
        #maxSpeed - min wait time
        #startSpeed - starting wait time
        curSpeed = startSpeed
        inc = (maxSpeed - curSpeed)/(count/2)
        
        for i in range(0, count):
            time.sleep(curSpeed)
            GPIO.output(self.pinList[2], GPIO.HIGH)
            time.sleep(curSpeed)
            GPIO.output(self.pinList[2], GPIO.LOW)
            if curSpeed > maxSpeed:
                curSpeed +=inc

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)
        #GPIO.output(self.pinList[1], GPIO.HIGH)
        #GPIO.output(self.pinList[0], GPIO.HIGH) #set enable high

    def cleanup(self):
          GPIO.cleanup()


class Machine_EasyDriver:
    
    def __init__(self, ad=[None,None,None,None,None,None]):
        self.activeDrinks = ad
        self.pinList = [2,3,4,17,27]
        

    def getDrinks(self):
        return self.activeDrinks
    
    def setDrink(self, drink, pos):
        self.activeDrinks[pos] = drink


    def step(self):
        time.sleep(0.001)
        GPIO.output(self.pinList[0], GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.pinList[0], GPIO.LOW)

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)

    def cleanup(self):
          GPIO.cleanup()


mac = Machine_BiggerDriver()
mac.setup()
curTime = datetime.datetime.now()
#mac.step_control(4000, .0002)
for i in range(0,2000):
    mac.step()
totalTime = datetime.datetime.now() - curTime
print("total {}".format(totalTime))
mac.cleanup()


'''
mac = Machine_EasyDriver()
mac.setup()
curTime = datetime.datetime.now()
for x in range(0,2000):
    mac.step()
totalTime = datetime.datetime.now() - curTime
print("total {}".format(totalTime))
mac.cleanup()
'''
