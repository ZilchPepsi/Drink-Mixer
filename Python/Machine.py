#!/usr/bin/python
import RPi.GPIO as GPIO
import time

'''
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


class Machine:
    
    def __init__(self, ad=[None,None,None,None,None,None]):
        self.activeDrinks = ad
        self.pinList = [2,3,4,17,27]
        

    def getDrinks(self):
        return self.activeDrinks
    def setDrink(self, drink, pos):
        self.activeDrinks[pos] = drink


    def step(self):
        GPIO.output(self.pinList[0], GPIO.HIGH)
        GPIO.output(self.pinList[0], GPIO.LOW)

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW)

    def cleanup(self):
          GPIO.cleanup()

mac = Machine()
mac.setup()
for x in range(0,400):
    mac.step()
    print("step {}".format(x))
mac.cleanup()

'''
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.5

# main loop

try:
    x = 0
    for i in pinList:
        x++
        GPIO.output(i, GPIO.LOW)
        print(x)
        time.sleep(SleepTimeL)
    GPIO.cleanup()
    print("Good bye!")
  #GPIO.output(2, GPIO.LOW)
  #print( "ONE")
  #time.sleep(SleepTimeL); 
  #GPIO.output(3, GPIO.LOW)
  #print ("TWO")
  #time.sleep(SleepTimeL);  
  #GPIO.output(4, GPIO.LOW)
  #print ("THREE")
  #time.sleep(SleepTimeL);
  #GPIO.output(17, GPIO.LOW)
  #print ("FOUR")
  #time.sleep(SleepTimeL);
  #GPIO.output(27, GPIO.LOW)
  #print ("FIVE")
  #time.sleep(SleepTimeL);
  #GPIO.output(22, GPIO.LOW)
  #print ("SIX")
  #time.sleep(SleepTimeL);
  #GPIO.output(10, GPIO.LOW)
  #print "SEVEN"
  #time.sleep(SleepTimeL);
  #GPIO.output(9, GPIO.LOW)
  #print "EIGHT"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
'''
