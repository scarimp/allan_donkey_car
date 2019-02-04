# Complete project details at https://RandomNerdTutorials.com
from machine import Pin, PWM
import machine
from time import sleep, ticks_ms, time
from hcsr04 import HCSR04
import os

try:
  import usocket as socket
except:
  import socket
  
import uselect
sel = uselect.poll()

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

# -----------------------------------------------------
# connection to local wifi
# ssid= your router id
# password = password to router

ssid = 'Vodafone-30663093'
password = 'LouiseOgJulie'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#----------------------------------------------
# global variables


startTime=time()
stopTime=time()
leftSpeed=100
rightSpeed=100
notconnect=True
oldRightSpeed=0
oldLeftSpeed=0
newRightSpeed=0
newLeftSpeed=0
firstSpeed=True
dir="stop"
speed=500
qarray=[0,0,0,0,0]
intSpeed=0.0
difSpeed=0.0
proSpeed=0.0
oldSpeed=0.0

led = Pin(17, Pin.OUT)
ledL1 = Pin(25,Pin.OUT)
ledL2 = Pin(33, Pin.OUT)
ledR1 = Pin(26,Pin.OUT)
ledR2 = Pin(27, Pin.OUT)
led_pwmL = PWM(Pin(16),30000)
led_pwmR = PWM(Pin(4),30000)

# -----------------------------------------------------
# five modules controll the movements of the robot: forward, backward, left, right, stop
# each module receives speed for left and right motor. 
# led_pwmL and led_pwmR sets speed of the motors
# ledL1, ledL2, ledR1 aqnd ledR2 controll the directions of the motors

def forward (speedL,speedR):
  #print(speedL)
  #print(speedR)
  led_pwmL.duty(int(speedL))
  led_pwmR.duty(int(speedR))
  ledL1.value(1)
  ledL2.value(0)
  ledR1.value(1)
  ledR2.value(0)
  print('forward')
  
  
def backward (speedL,speedR):
  led_pwmL.duty(int(speedL))
  led_pwmR.duty(int(speedR))
  ledL1.value(0)
  ledL2.value(1)
  ledR1.value(0)
  ledR2.value(1)
  print('backward')
  
  
def stop ():
  global counterL
  global counterR
  led_pwmL.duty(0)
  led_pwmR.duty(0)
  ledL1.value(0)
  ledL2.value(0)
  ledR1.value(0)
  ledR2.value(0)
  counterL=0
  counterR=0
  
def right (speedL,speedR):
  led_pwmL.duty(int(speedL*0.8))
  led_pwmR.duty(int(speedR*0.8))
  ledL1.value(1)
  ledL2.value(0)
  ledR1.value(0)
  ledR2.value(0)
  print('right')
  
  
def left (speedL,speedR):
  led_pwmL.duty(int(speedL*0.8))
  led_pwmR.duty(int(speedR*0.8))
  ledL1.value(0)
  ledL2.value(0)
  ledR1.value(1)
  ledR2.value(0)
  print('left')
  
  
  # ---------------------------------------
  # the following modules modify the speed on each wheel (R and L) based on
  # a simple PID implementation
  # I module proportional (difference, sum, dir) the variable kp, ki and kd are set - a value between 0 and 1. 
  # normally kp+ki+kd should be less than 1
  # module proportional calls module checksmovements(dir) whichs initiate the command to the motors

def updateArray(newSpeed):
  global qarray
  i=4
  while i>0:
    qarray[i]=qarray[i-1]*0.5
    i=i-1
  qarray[0]=newSpeed
  

def integration(newSpeed):
   global qarray
   global intSpeed
   updateArray(newSpeed)
   total=0
   i=5
   while i>0:
     i=i-1
     total=total+qarray[i]
     
   intSpeed=total/2  
   
   
def differential(newSpeed,oldSpeed):  
   global difSpeed
   if oldSpeed>0:
     difSpeed=oldSpeed-newSpeed
   else: 
     difSpeed=0.0   

   
def proportional (difference, sum, dir):
  global firstSpeed
  global speed
  global leftSpeed
  global rightSpeed
  global oldRightSpeed
  global oldLeftSpeed
  global newRightSpeed
  global newLeftSpeed
  global intSpeed
  global difSpeed
  global proSpeed
  global oldSpeed
  kp=0.0
  ki=0.0
  kd=0.0
  
  if sum==0:
    sum=1
  newSpeed= (difference*2/sum)*100 
  integration(newSpeed)
  differential(newSpeed,oldSpeed)
  proSpeed=newSpeed
  oldSpeed=newSpeed
  newSpeed=kp*proSpeed+ki*intSpeed+kd*difSpeed
  #print(proSpeed)
  #print(intSpeed)
  #print(difSpeed)
  #print(newSpeed)
  leftSpeed=100+newSpeed
  rightSpeed=100-newSpeed
  if firstSpeed:
    newRightSpeed=int(speed*rightSpeed/100)
    newLeftSpeed=int(speed*leftSpeed/100)
    print("firstSpeed")
    firstSpeed=False
  else: 
    newRightSpeed=int(oldRightSpeed*rightSpeed/100)
    newLeftSpeed=int(oldLeftSpeed*leftSpeed/100)   
  checkMovements(dir)
  oldLeftSpeed=newLeftSpeed
  oldRightSpeed=newRightSpeed

  
  
def checkMovements(dir):
  global newRightSpeed
  global newLeftSpeed
  if dir=="forward": 
         forward(newLeftSpeed, newRightSpeed)
  elif dir=="backward":
         backward(newLeftSpeed, newRightSpeed)
  if dir=="left":
         left(newLeftSpeed, newRightSpeed)   
  elif dir=="right":
         right(newLeftSpeed, newRightSpeed)   
 
 
def speedCalc(valueString):
  global speed
  global firstSpeed
  # indexL=valueString.find('/?value')
  indexH=valueString.find('&')
  try:
    #print(valueString[14:indexH])
    value=int(valueString[14:indexH])
    if value<26: speed=500
    if value>25 and value<51: speed=700
    if value>50 and value<76: speed=900
    if value>75 and value<101: speed=1000
  except:
    speed=800;  
  #print(speed)
  firstSpeed=True
 

  
# ---------------------------------------------------- 
# The ultrasonic sensor triggers interrupt using the timer-module. 
# When callback to distance(minDistance) the module BackAway is called and the 
# robot goes back for 2 seconds and turn left/forward for 1 second 
# parameters are changed in these two modules
  
def backAway():
  backward(400,400)
  sleep(2)
  left(400,400)
  sleep(1)
  stop()

sensor = HCSR04(trigger_pin=2, echo_pin=15)

def distance(minDistance):
  distance = sensor.distance_cm()
  if distance<minDistance and distance>0:
    backAway()

timer=machine.Timer(3)

def handleInterrupt(timer):
  distance(30.0)

  
timer.init(period=500, mode=machine.Timer.PERIODIC, callback=handleInterrupt) 


# --------------------------------------------------------
# the optical encoder connects two interrups on pin 5 and pin 19
# the global variales counterL and counterR increments with each interrupt call


def count(p):
  global counterL
  global counterR
  if p==Pin(5):
    sleep(0.01)
    counterL=counterL+1
    #print("countL") 
  if p==Pin(19):
    sleep(0.008)
    counterR=counterR+1
    #print("countR")

  
counterL=0
counterR=0
stroboL=machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
stroboR=machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
stroboL.irq(trigger=machine.Pin.IRQ_FALLING, handler=count)
stroboR.irq(trigger=machine.Pin.IRQ_FALLING, handler=count)


  
#--------------------------------------------------
#web_page is the html code for the clients web page

 
def web_page():

  
  html = """<!DOCTYPE HTML><html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><link rel=\"icon\" href=\"data:,\"><style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}        .button { -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; background-color: #4CAF50;  border: none; color: white; padding: 12px 28px; text-decoration: none; font-size: 26px; margin: 1px; cursor: pointer;}.button2 {background-color: #555555;}</style><script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script></head>
            <p><button class=\"button\" onclick=\"moveForward()\">FORWARD</button></p>
            <div style=\"clear: both;\"><p><button class=\"button\" onclick=\"moveLeft()\">LEFT </button>
            <button class=\"button button2\" onclick=\"stopRobot()\">STOP</button>
            <button class=\"button\" onclick=\"moveRight()\">RIGHT</button></p></div>
            <p><button class=\"button\" onclick=\"moveReverse()\">REVERSE</button></p>
            <p>Motor Speed: <span id=\"motorSpeed\"></span></p>         
            <input type=\"range\" min=\"0\" max=\"100\" step=\"25\" id=\"motorSlider\" onchange=\"motorSpeed(this.value)\" value=\"" + valueString + "\"/>
            
            <script>$.ajaxSetup({timeout:1000});
            function moveForward() { $.get(\"/forward\"); {Connection: close};}
            function moveLeft() { $.get(\"/left\"); {Connection: close};}
            function stopRobot() { $.get(\"/stop\"); {Connection: close};}
            function moveRight() { $.get(\"/right\"); {Connection: close};}
            function moveReverse() { $.get(\"/reverse\"); {Connection: close};}
            var slider = document.getElementById(\"motorSlider\");
            var motorP = document.getElementById(\"motorSpeed\"); motorP.innerHTML = slider.value;
            slider.oninput = function() { slider.value = this.value; motorP.innerHTML = this.value; }
            function motorSpeed(pos) { $.get(\"/?value=\" + pos + \"&\"); {Connection: close};}</script>
           
            </html>"""
  return html
  
  
# accept_wrapper is called when the web client inputs anything with sel.poll(100) 
# this module checks the connection, gets the new input and updates the client-page
# calls motorDirections(request) with the input from web
# motorDirections checks direction and sets global variable: dir
  
def accept_wrapper(s):
   request=''
   try:
     conn, addr = s.accept()
     print('Got a connection from %s' % str(addr))
     conn.setblocking(False)
     request = conn.recv(30)
   except OSError:
     print("Caught OSError: EAGAIN")
     
   request = str(request)
   #print(request)
   response = web_page()
   t=0
   while len(response)-t>0:
     t=conn.send(response)
     #print(t)
   
   print('web afsendt')
   motorDirections(request)
   conn.close()
  
  

def motorDirections(request):
  global speed
  global dir
  if request.find('/forward')>0:
      #forward(speed,speed)
      dir="forward"
  if request.find('/reverse')>0:
      #backward(speed,speed)
      dir="backward"
  if request.find('/stop')>0:
      stop()
      dir="stop"
  if request.find('/right')>0:
      #right(speed,speed)
      dir="right"
  if request.find('/left')>0:
      #left(speed,speed)
      dir="left"
  if request.find('/?value')>0:
      #print('speed')
      speedCalc(request[:20])
  
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print('listening on')
#s.setblocking(False)
sel.register(s, uselect.POLLIN)


# --------------------------------------------
# main loop:
# listens for inputs from web and initiates the movements through call of 
# proportional() and checkmovements()
# waits half a second for next iteration (only due to printings for debugging

while True:
  events = sel.poll(100)
  print(events)
  for key, mask in events:
        accept_wrapper(s)
  
  #if counterL>0 or counterR>0:
  #  print(counterL)
  #  print(counterR)
  #print(dir)
  if dir=="forward" or dir=="backward":
    proportional(counterR-counterL, counterR+counterL, dir)
  else:
    checkMovements(dir)  
  counterL=0
  counterR=0
  sleep(0.1)














