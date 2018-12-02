from threading import Thread
import signal
import RPi.GPIO as GPIO
from time import sleep

import motors.m5
import motors.m6

#import sound.control
#import light.control

GPIO.setmode(GPIO.BCM)



def szene1():
#    motors.m4.stop()
    motors.m5.init(1000)
    motors.m6.init(1000)
    motors.m5.stop()
    motors.m6.stop()
    #motors.m1.right(2.25)
    #sleep(5)

    #motors.m5.left(10)
    motors.m6.right(10)
 
    motors.m6.stop()
    #sleep(10)

   # motors.m4.init(500)
    #T = Thread(target=motors.m4.left, args=[1])
    #T.start()


def main():
    try:
        szene1()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()