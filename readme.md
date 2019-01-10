
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
