# Complete project details at https:github.com/scarimp/allan_donkey_car

from machine import Pin
from time import sleep, ticks_ms, time
import machine

import os
import ssd1306A
i2c = machine.I2C(scl=machine.Pin(18), sda=machine.Pin(22))
oled = ssd1306A.SSD1306_I2C(128, 64, i2c, 0x3c)

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

oledshow('test test test',2)










