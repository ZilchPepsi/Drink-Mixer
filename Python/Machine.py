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

    drinkWaitTime = 5 #TODO - needs testing
    mixerWaitTime = 2 #TODO - needs testing

    maxSpeed = .00035 #max speed of stepper motor
    #enable low is right, high is left

    
    def __init__(self, dp=[0,0,0,0,0,0]):
        startPosition = 0
        currentPosition = 0
        drinkPositions = dp
        setup()


    def getDrinkPositions(self):
        return (startPosition, drinkPositions)

    def setDrinkPosition(self, drinkNum, pos):
        drinkPosition[drinkNum] = pos


    def openAlc(self, drinkNum):
        GPIO.output(relayDrinkPins[drinkNum], GPIO.LOW)
        time.sleep(drinkWaitTime)
        GPIO.output(relayDrinkPins[drinkNum],  GPIO.HIGH)
        time.sleep(1)

    def openMixer(self, drinkNum):
        GPIO.output(relayMixerPins[drinkNum], GPIO.LOW)
        time.sleep(mixerWaitTime)
        GPIO.output(relayMixerPins[drinkNum],  GPIO.HIGH)
        time.sleep(1)

    #rotates stepper motor 'rotations' times
    def moveTrayR(self, rotations):
        _step_control(rotations, maxSpeed)

    #moves tray to position 'position'
    def moveTrayP(self, position):

        if position < 0 or position > len(drinkPositions): # this position is out of range
            print("tried to move to position {}, which does not exist".format(position))
            return
        
        numRot = 0  
        if position == 0:
            numRot = -currentPosition
        else:    
            numRot = drinkPositions[position-1]- currentPosition
        _step_control(numRot, maxSpeed)
        
    def resetPosition(self):
        _step_control(-currentPosition, maxSpeed)


    def _step_control(self, count, maxS, startSpeed = .001):
        #count - number of rotations
        #maxSpeed - min wait time
        #startSpeed - starting wait time
        curSpeed = startSpeed
        inc = (maxS-startSpeed)/(count/2)

        if count ==0:
            return
        elif count <0 :
            GPIO.output(stepperPins[1], GPIO.HIGH)
            count = count*-1
        else:
            GPIO.output(stepperPins[1], GPIO.LOW)
        
        for i in range(0, count):
            time.sleep(curSpeed)
            GPIO.output(stepperPins[2], GPIO.HIGH)
            time.sleep(curSpeed)
            GPIO.output(stepperPins[2], GPIO.LOW)
            if curSpeed > maxS:
                curSpeed += math.exp(curStep*inc)*inc*10
                if curSpeed < maxS:
                    curSpeed = maxS

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in stepperPins:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)
        for i in relayDrinkPins:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.HIGH)
        for i in relayMixerPins:
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
            curSpeed += math.exp(curStep*inc)*inc*10
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
            curSpeed += math.exp(curStep*inc)*inc*10
            if curSpeed < maxS:
                curSpeed = maxS
