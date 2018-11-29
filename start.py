import motors.m1
import RPi.GPIO as GPIO
import sound.control
import light.control
from threading import Thread
import signal

def intro():
    sound.control.text1()

def szene1():
    light.control.l1_on()
    sound.control.text2()
    T = Thread(target=sound.control.lied1)
    T.start()
    motors.m1.init(100)
    motors.m1.right(1)
    motors.m1.stop()





def main():
    try:
        intro()
        szene1()    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
