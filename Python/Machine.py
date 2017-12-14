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

low->high = step

motor colors : driver wires
black : purple
green : brown
red : red
blue : black
'''

class Machine:

    drinkPositions = []
    startPosition = 0
    currentPostion = 0
    stepperPins = [2,3,4]
    relayDrinkPins = [17, 18, 22, 23, 24, 27]
    relayMixerPins = [9,10,11,25]

    drinkWaitTime = 2 #TODO - needs testing
    mixerWaitTime = 1 #TODO - needs testing

    maxSpeed = .0004 #max speed of stepper motor
    #enable low is right, high is left

    
    def __init__(self, dp=[0,0,0,0,0,0]):
        self.startPosition = 0
        self.currentPosition = 0
        self.drinkPositions = dp
        self.setup()


    def getDrinkPositions(self):
        return (startPosition, drinkPositions)

    #drinks are origin 1
    def setDrinkPosition(self, drinkNum, pos):
        self.drinkPositions[drinkNum-1] = pos


    #origin 1
    def openAlc(self, drinkNum):
        GPIO.output(self.relayDrinkPins[drinkNum-1], GPIO.LOW)
        time.sleep(self.drinkWaitTime)
        GPIO.output(self.relayDrinkPins[drinkNum-1],  GPIO.HIGH)
        time.sleep(1)
    #origin 1
    def openMixer(self, drinkNum):
        GPIO.output(self.relayMixerPins[drinkNum-1], GPIO.LOW)
        time.sleep(self.mixerWaitTime)
        GPIO.output(self.relayMixerPins[drinkNum-1],  GPIO.HIGH)
        time.sleep(1)

    #rotates stepper motor 'rotations' times
    def moveTrayR(self, rotations):
        self.currentPosition +=rotations
        self._step_control(rotations, self.maxSpeed)

    #moves tray to position 'position', drinks are origin 1
    #moving to pos 0 means start
    def moveTrayP(self, position):
        if position < 0 or position > len(self.drinkPositions): # this position is out of range
            print("tried to move to position {}, which does not exist".format(position))
            return
        
        numRot = 0  
        if position == 0:
            numRot = -self.currentPosition
            self.currentPosition = 0
            
        else:    
            numRot = self.drinkPositions[position-1]- self.currentPosition
            self.currentPosition += numRot
        self._step_control(numRot, self.maxSpeed)
        
    def resetPosition(self):
        self._step_control(-self.currentPosition, self.maxSpeed)


    def _step_control(self, default_count, maxS, startSpeed = .001):
        #count - number of rotations
        #maxSpeed - min wait time
        #startSpeed - starting wait time
        
        count = abs(default_count)
        curSpeed = startSpeed
        inc = (maxS-startSpeed)/(count/2)

        if default_count ==0:
            return
        elif default_count <0 :
            GPIO.output(stepperPins[1], GPIO.HIGH)
        else:
            GPIO.output(stepperPins[1], GPIO.LOW)

        print("count {}".format(count))
        for i in range(0, count):
            time.sleep(curSpeed)
            GPIO.output(stepperPins[2], GPIO.HIGH)
            time.sleep(curSpeed)
            GPIO.output(stepperPins[2], GPIO.LOW)
            if curSpeed > maxS:
                curSpeed += math.exp(curSpeed*inc)*inc*10
                if curSpeed < maxS:
                    curSpeed = maxS

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.stepperPins:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)
        for i in self.relayDrinkPins:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.HIGH)
        for i in self.relayMixerPins:
            GPIO.setup(i,GPIO.OUT, initial = GPIO.HIGH)

    #main calls me when we're done
    def cleanup(self):
          GPIO.cleanup()

#enable, direction, pulse
stepperPins = [2,3,4]
enabled = True

def moveLeft_debug(maxS, startSpeed = .001):
    curSpeed = startSpeed
    inc = (maxS-startSpeed)/5
    GPIO.output(stepperPins[1], GPIO.HIGH)

    while enabled:
        time.sleep(curSpeed)
        GPIO.output(stepperPins[2], GPIO.HIGH)
        time.sleep(curSpeed)
        GPIO.output(stepperPins[2], GPIO.LOW)
        if curSpeed > maxS:
            curSpeed += math.exp(curSpeed*inc)*inc*10
            if curSpeed < maxS:
                curSpeed = maxS

def moveRight_debug(maxS, startSpeed = .001):
    curSpeed = startSpeed
    inc = (maxS-startSpeed)/5
    GPIO.output(stepperPins[1], GPIO.LOW)

    while enabled:
        time.sleep(curSpeed)
        GPIO.output(stepperPins[2], GPIO.HIGH)
        time.sleep(curSpeed)
        GPIO.output(stepperPins[2], GPIO.LOW)
        if curSpeed > maxS:
            curSpeed += math.exp(curSpeed*inc)*inc*10
            if curSpeed < maxS:
                curSpeed = maxS

'''
mac = Machine()
#def setDrinkPosition(self, drinkNum, pos):
mac.setDrinkPosition(1, 6200)
mac.setDrinkPosition(2, 13200)
mac.setDrinkPosition(3, 20400)
mac.setDrinkPosition(4, 27700)
mac.setDrinkPosition(5, 34700)
mac.setDrinkPosition(6, 40500)
mac.moveTrayP(2)
#mac.moveTrayR(50)
mac.openAlc(1)
time.sleep(1)
mac.moveTrayP(0)
mac.cleanup()
'''
