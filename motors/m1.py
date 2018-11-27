from time import sleep
import RPi.GPIO as GPIO
from __future__ import division

GPIO.setmode(GPIO.BCM)

# Verwendete Pins des ULN2003A auf die Pins des Rapberry Pi
# zugeordnet
IN1 = 6 # IN1
IN2 = 13 # IN2
IN3 = 19 # IN3
IN4 = 26 # IN4

# Wartezeit regelt die Geschwindigkeit wie schnell sich der Motor
# dreht.
TIME = 0.001
LEFT = 0
RIGHT = 0

# Der Schrittmotoren 28BYJ-48 ist so aufgebaut, das der Motor im
# Inneren 8 Schritte für eine Umdrehung benötigt. Durch die Betriebe
# benätigt es aber 512 x 8 Schritte damit die Achse sich einmal um
# sich selbt also 360° dreht.

# Definition der Schritte 1 - 8 über die Pins IN1 bis IN4
# Zwischen jeder Bewegung des Motors wird kurz gewartet damit der
# Motoranker seine Position erreicht.
def Step1():
    GPIO.output(IN4, True)
    sleep (TIME)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (TIME)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (TIME)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (TIME)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (TIME)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (TIME)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (TIME)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (TIME)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Umdrehung links herum
def left():
  global LEFT
  LEFT = 1;
  while LEFT >= 1:
    Step1()
    Step2()
    Step3()
    Step4()
    Step5()
    Step6()
    Step7()
    Step8()

# Umdrehung rechts herum
def right():
  global RIGHT
  RIGHT = 1
  while RIGHT >= 1:
    Step8()
    Step7()
    Step6()
    Step5()
    Step4()
    Step3()
    Step2()
    Step1()

def stop():
  global RIGHT
  global LEFT
  LEFT = 0
  RIGHT = 0
  GPIO.output(IN1, False)
  GPIO.output(IN2, False)
  GPIO.output(IN3, False)
  GPIO.output(IN4, False)
  
def init(speed):
  global TIME;
  # Pins aus Ausgänge definieren
  GPIO.setup(IN1,GPIO.OUT)
  GPIO.setup(IN2,GPIO.OUT)
  GPIO.setup(IN3,GPIO.OUT)
  GPIO.setup(IN4,GPIO.OUT)

  # Alle Pins werden initial auf False gesetzt. So dreht sich der
  # Stepper-Motor nicht sofort irgendwie.
  stop()
  TIME = 1/speed;