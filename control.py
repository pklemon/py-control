from threading import Thread
import signal
import RPi.GPIO as GPIO
from time import sleep
import pyxhook

import motors.m1
import motors.m2
import motors.m3
import motors.m4
import motors.m5
import motors.m6
import sound.control
import light.control


def intro():
    sound.control.text1()

def szene1():
    light.control.l1_on()
    sound.control.text2()

    motors.m1.init(800)
    T = Thread(target=motors.m1.right, args=[3])
    T.start()

    sound.control.lied1()
    light.control.l1_off()

    motors.m1.init(1000)
    T = Thread(target=motors.m1.left, args=[3])
    T.start()

def szene2():
    light.control.l2_on()
    sound.control.text3()

    motors.m2.init(1000)
    T = Thread(target=motors.m2.left, args=[9])
    T.start()

    sleep(5)

    sound.control.lied2()

    motors.m2.init(1000)
    T = Thread(target=motors.m2.left, args=[9.75])
    T.start()

    sleep(15)

    light.control.l2_off()
    sleep(20)

def szene3():
    light.control.l3_on()
    T = Thread(target=sound.control.text4)
    T.start()
    motors.m3.init(1000)
    motors.m3.right(11)
    sound.control.lied3_1()
    motors.m3.right(5)
    sound.control.lied3_2()
    motors.m3.right(6)
    sound.control.lied3_3()

    motors.m3.init(1000)
    T = Thread(target=motors.m3.right, args=[20.5])
    T.start()

    sleep(20)

    light.control.l3_off()

def szene4():
    light.control.l4_on()
    sound.control.text5()
    light.control.l4_off()

def szene5():
    sound.control.text6()
    light.control.l5_on()

    motors.m4.init(800)
    T = Thread(target=motors.m4.right, args=[2.25])
    T.start()

    sound.control.lied4()

    motors.m4.init(1000)
    T = Thread(target=motors.m4.left, args=[2.25])
    T.start()

    light.control.l5_off()

def szene6():
    light.control.l6_on()
    sound.control.text7()

    motors.m5.init(100)
    T = Thread(target=motors.m5.right, args=[1])
    T.start()

    motors.m6.init(100)
    T2 = Thread(target=motors.m6.right, args=[1])
    T2.start()

    sleep(10)

    light.control.l6_off()

    motors.m5.init(1000)
    T = Thread(target=motors.m5.left, args=[1])
    T.start()

    motors.m6.init(1000)
    T2 = Thread(target=motors.m6.left, args=[1])
    T2.start()

    
def licht_on():
    light.control.l1_on()
    light.control.l2_on()
    light.control.l3_on()
    light.control.l4_on()
    light.control.l5_on()
    light.control.l6_on()

def licht_off():
    light.control.l1_off()
    light.control.l2_off()
    light.control.l3_off()
    light.control.l4_off()
    light.control.l5_off()
    light.control.l6_off()

def mainSequence():
  licht_off()
  intro()
  szene1()
  szene2()
  szene3()
  szene4()
  sleep(3)
  szene5()
  szene6()
  sleep(10)
  licht_on()

def kbevent(event):
  global running
  print(event.ScanCode)
  code = event.ScanCode
  

  if code == 90
    running = False

  if code == 89
    licht_on()
  
  if code == 91
    licht_off()

  if code == 104
    s = Thread(target=mainSequence)
    s.start()

  if code == 77
    motors.m1.init(1000)
    motors.m1.left(0.25)
    motors.m1.stop()
  
  if code == 106
    motors.m1.init(1000)
    motors.m1.right(0.25)
    motors.m1.stop()

  if code == 63
    motors.m2.init(1000)
    motors.m2.left(0.25)
    motors.m2.stop()
  
  if code == 82
    motors.m2.init(1000)
    motors.m2.right(0.25)
    motors.m2.stop()

  if code == 79
    motors.m3.init(1000)
    motors.m3.left(0.25)
    motors.m3.stop()
  
  if code == 80
    motors.m3.init(1000)
    motors.m3.right(0.25)
    motors.m3.stop()

  if code == 81
    motors.m4.init(1000)
    motors.m4.left(0.25)
    motors.m4.stop()
  
  if code == 86
    motors.m4.init(1000)
    motors.m4.right(0.25)
    motors.m4.stop()
  
  if code == 83
    motors.m5.init(1000)
    motors.m5.left(0.25)
    motors.m5.stop()
  
  if code == 84
    motors.m5.init(1000)
    motors.m5.right(0.25)
    motors.m5.stop()

  if code == 85
    motors.m6.init(1000)
    motors.m6.left(0.25)
    motors.m6.stop()
  
  if code == 22
    motors.m6.init(1000)
    motors.m6.right(0.25)
    motors.m6.stop()


hm = pyxhook.HookManager()
hm.KeyDown = kbevent
hm.HookKeyboard()
hm.start()

running = True
while running
  sleep(0.1)

hookman.cancel()