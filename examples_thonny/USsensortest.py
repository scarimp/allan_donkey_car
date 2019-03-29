# Complete project details at https:github.com/scarimp/allan_donkey_car

from machine import Pin, PWM
from time import sleep, ticks_ms, time
import machine
from hcsr04B import HCSR04
import os
import ssd1306A
i2c = machine.I2C(scl=machine.Pin(18), sda=machine.Pin(22))
oled = ssd1306A.SSD1306_I2C(128, 64, i2c, 0x3c)


import network

import esp
esp.osdebug(None)

import gc
gc.collect()

oledtext=[0,1,2,3,4]


def oledshow(otext,line):
  global oledtext
  oledtext[line]=otext
  
  oled.fill(0)
  for j in range(0,5):
    oled.text(str(oledtext[j]),0,10*j)
  oled.show()

  
# ---------------------------------------------------- 
# The ultrasonic sensor triggers interrupt using the timer-module. 
# When callback to distance(minDistance) the module BackAway is called and the 
# robot goes back for 2 seconds and turn left/forward for 1 second 
# parameters are changed in these two modules


sensor = HCSR04(trigger_pin=2, echo_pin=15)



def showDistance():
  distance = sensor.distance_cm()
  oledshow('Distance:',3)
  oledshow(str(distance),4) 

timer=machine.Timer(2)

def handleInterrupt(timer):
  showDistance()

  
timer.init(period=500, mode=machine.Timer.PERIODIC, callback=handleInterrupt) 

 





















