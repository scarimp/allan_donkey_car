

Doc on ESP32 [THONNY MODULES](https://github.com/scarimp/allan_donkey_car/blob/master/SHELL%20TONNY%20MODULES-ON_ESP32.pdf).

Another python for iot devicesan; article on tonny from realpython [thonny](https://realpython.com/python-thonny/). Here documentation and [site](https://thonny.org/). Here the citation from [ruis Santos](https://rntlab.com/product/micropython-programming-with-esp32-and-esp8266/); and here the repository on github of [plugin of thonny](https://github.com/thonny) for esp32 et similia, and finally [here](https://github.com/thonny/thonny/wiki/MicroPython) for installing the plugin for esp32.
Another article of Ruis Santos on [thonny](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/).Using esptool to flash [firmware](https://github.com/espressif/esptool) on esp32 devices.


-------------------------------------------------------------------------------------
Foe examples on python [see](https://randomnerdtutorials.com/micropython-interrupts-esp32-esp8266/).

Rimember that you can use [platformIO for esp32](https://github.com/espressif/arduino-esp32/blob/master/docs/platformio.md).
------------------------------------------------------------
And finally the [RC CAR](http://a.wiphone.io/?utm_source=DigitalOcean_Newsletter)

Esp32 pin [layout](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)

Problems with connection of esp32 to pc windows [see this ](https://randomnerdtutorials.com/esp32-troubleshooting-guide/) and this [siliconlabs](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers).Here to dowbload the [firmware](https://micropython.org/download#esp8266).

A **FireBeetle ESP32 IOT** Microcontroller (Supports Wi-Fi & Bluetooth)from [dfrobot](https://www.dfrobot.com/product-1590.html)
with USB and 3.7V external lithium battery. And both USB and external DC can charge the Lipo battery directly.

A plug-in  Esp32 and Esp3286 for micro-python [Thonny](https://github.com/thonny/thonny-esp) and [here](https://github.com/thonny/thonny/wiki/MicroPython).

Computer vision via pytorch (*torchvision*) on raspeberry pi (Ubuntu MATE 16.04) for [racing car ](https://github.com/sergionr2/RacingRobot)

[ESP-WHO](https://www.espressif.com/en/products/hardware/esp-eye/overview)

ESP-WHO is a face detection and recognition platform that is currently based on Espressif Systems' ESP32 chip.

Espressif ha rilasciato la nuova scheda di sviluppo AIoT per applicazioni relative all'Intelligenza Artificiale 
e all'Internet degli oggetti completa di fotocamera digitale, microfono e Wi-Fi. 
ESP-EYE, la nuova scheda di sviluppo AIoT 


See:[ESP-who](https://github.com/espressif/esp-who)


[A car drive simulator](http://carla.org/?ck_subscriber_id=272173535) is also open source:There is a : [CARLA Autonomous Driving Challenge](https://carlachallenge.org/).

[*Building a Toy Self-Driving Car: Part 1*](https://blog.floydhub.com/toy-self-driving-car-part-one/?utm_source=blog_subscribers&utm_medium=email&utm_campaign=2019_02_07)

Learn the history and technology of autonomous cars in this Part 1 of a series on building a self-driving toy car with Raspberry Pi, Keras, and FloydHub.

Discussion with Anders about a data logger with [motion detection](https://randomnerdtutorials.com/hack-pir-motion-sensor-esp8266-hlk-pm03/).


(04/02/2019) Allan  add  the python  project on the car developed with uPyCraft IDE:
---------------------------------------------


Hardware Basic:
-----------------
* TT model
* 2 dc motors
* 1 motordriver l....
* 1ESP32 mcu
* Battery: 4 x 1.5 volt (up to at total of 12 V)

Add on:
1. Ultrasonic sensor - hcrso4
2. Optical encoders - 

General description of car:
--------------------------
Two wheeled car with caster wheel at the back.
The MCU connects web-page (local) with the motor controll. 
Allowing for four directions and stop as well as controll of speed.

Basic configuration:
The car is controlled via webpage. 

Obstacle avoidance:
-------------------
Add on to the basic configuration: Using the ultrasonic sensor. 
The car stops when meeting obstacles in front (e.g. 30 cm distance) - then 
it backs and turn left before continuing forward. The signal is 
overriding the web set parameters for this maneuvre, using interupt signal.

PID control:
------------
Add on to the obstacle avoidance configuration: Using the optical encoder. 
The program reads the two encoders and based on the difference between 
the two sets of data, the motor speed is controlled. 
The program use a simple implementation of the [PID routine](https://en.wikipedia.org/wiki/PID_controller) or [Controllo PID](https://it.wikipedia.org/wiki/Controllo_PID).

Programmes:
-----------
1. PID control, **robot_with_encoder_v1.py**                   
2. Obstacle avoidance, **robot_with_ultrasonic_v1.py**
3. Basic configuration, **robot_with_web_v1.py**
 
*Here the main loop of PID control:*
~~~~
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
~~~~

Complete project details [at RandomNerdTutorials](https://RandomNerdTutorials.com)

Thonny another [IDE](https://thonny.org/) for micropython on esp32 and esp8266.

----------------------------------------------------------

(10/01/2019) Franco add  this news on uPyCraft IDE:
---------------------------------------------


Getting Started with MicroPython on ESP32 and ESP8266

Installing [uPyCraft IDE  repository](https://github.com/DFRobot/uPyCraft).

Documentation on [uPyCraft IDE](http://docs.dfrobot.com/upycraft/).

Is a simple  [python framework ](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/).
There is a payed course on micropython on the esp32 and esp8266.

I create a pdf about uPyCraft IDE, that is this repository [here](https://github.com/scarimp/allan_donkey_car/blob/master/uPyCraft%20IDE_MicroPython%20on%20ESP32%20and%20ESP8266.pdf).

A good blog about [uPyCraft IDE ](https://techtutorialsx.com/2017/07/20/esp32-micropython-getting-started-with-the-upycraft-ide/).

An example code on [GPIO](https://randomnerdtutorials.com/micropython-gpios-esp32-esp8266/), discussed also on the [forum](https://www.dfrobot.com/forum/viewtopic.php?f=20&t=16123).


----------------------------------------------------------------------------------------------------------
(09/01/2019) Franco add  this contribute:
---------------------------------------------
An esp32 device with camera:

Add an eye to esp32 board and ...:[eyes:](https://github.com/espressif/esp-who/blob/master/docs/en/get-started/ESP-EYE_V2.0_Getting_Started_Guide.md)
GitHub espressif/esp-who

Face detection and recognition framework. 

---------------------------------------------

(09/01/2019) Anders add  this contribute:
------------------------------------------
Hi Franco and Allan

I have found and read this book: 
Programming with MicroPython Embedded Programming with Microcontrollers and Python Nicholas H. Tollervey
Lots of inspiration allthough only a few examples for esp32.  
You can download it for free [here](http://www.allitebooks.in/programming-with-micropython/)


Google Play Books is a very fine reader for pdf-books
-- 
Anders Harbo

==================================================


Da: Allan Herman [mailto:teacher.physics@gmail.com] 
Inviato: sabato 24 novembre 2018 12:40
A: Francesco Luzio <f.luzio@converge.it>
Oggetto: Is this how you want me to communicate regarding my problems?

Ciao Francesco,
Is this what you want me to send when I have a problem:
1) I start with ssh and show that everything works.
2) A quit with Crtl-Z.
3) I try to start with: python manage.py drive
4) And you see the result in blue.
5) I found this link and it seems relevant line in extra-large letters:
https://www.raspberrypi.org/forums/viewtopic.php?t=117247
Allan


allan@Herman:~$ ssh pi@donkeypi
pi@donkeypi's password: 
Linux donkeypi 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 22 07:53:46 2018 from 192.168.1.8
(env) pi@donkeypi:~ $ cd ~/mycar
(env) pi@donkeypi:~/mycar $ python manage.py drive
using donkey version: 2.5.8 ...
/usr/lib/python3/dist-packages/h5py/__init__.py:34: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
loading config file: /home/pi/mycar/config.py
config loaded
PiCamera loaded.. .warming camera
Starting Donkey Server...
You can now go to http://192.168.1.5:8887 to drive your car.
/home/pi/env/lib/python3.5/site-packages/picamera/encoders.py:544: PiCameraResolutionRounded: frame size rounded up from 160x120 
mmal: mmal_vc_port_enable: failed to enable port 
vc.null_sink:in:0(OPQV): ENOSPC
mmal: mmal_port_enable: failed to enable connected port (vc.null_sink:in:0(OPQV))0x2192130 (ENOSPC)

(env) pi@donkeypi:~/mycar $ sudo reboot now
Connection to donkeypi closed by remote host.
Connection to donkeypi closed.
allan@Herman:~$ ssh pi@donkeypi
