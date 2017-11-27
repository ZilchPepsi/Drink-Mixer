#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import math

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
        #234 - stepper
        #17, 18, 22, 23, 24, 27 - relay
        self.pinList = [2,3,4, 17, 18, 22, 23, 24, 27]
        
        

    def getDrinks(self):
        return self.activeDrinks
    
    def setDrink(self, drink, pos):
        self.activeDrinks[pos] = drink


    def step(self):
        time.sleep(0.0004)
        GPIO.output(self.pinList[2], GPIO.HIGH)
        time.sleep(0.0004)
        GPIO.output(self.pinList[2], GPIO.LOW)

    def step_control(self, count, maxSpeed, startSpeed = .001):
        #count - number of rotations
        #maxSpeed - min wait time
        #startSpeed - starting wait time
        curSpeed = startSpeed
        inc = (maxSpeed-startSpeed)/(count/2)
        curStep = 1
        
        print("inc {}".format(inc))
        for i in range(0, count):
            time.sleep(curSpeed)
            GPIO.output(self.pinList[2], GPIO.HIGH)
            time.sleep(curSpeed)
            GPIO.output(self.pinList[2], GPIO.LOW)
            if curSpeed > maxSpeed:
                curSpeed += math.exp(curStep*inc)*inc*10
                curStep+=1
                if curSpeed < maxSpeed:
                    curSpeed = maxSpeed

    def openDrink(self, i):
        GPIO.output(self.pinList[2+i], GPIO.LOW)
        time.sleep(2)
        GPIO.output(self.pinList[2+i],  GPIO.HIGH)       

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)
        GPIO.output(self.pinList[3], GPIO.HIGH)
        GPIO.output(self.pinList[4], GPIO.HIGH)#set drink 1 high
        #GPIO.output(self.pinList[1], GPIO.HIGH) #changes direction
        #GPIO.output(self.pinList[0], GPIO.HIGH) #set enable high

    def cleanup(self):
          GPIO.cleanup()


mac = Machine_BiggerDriver()
mac.setup()
curTime = datetime.datetime.now()
#mac.step_control(200, .0003)
#for i in range(0,2000):
    #mac.step()
mac.openDrink(1)
mac.openDrink(2)
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
