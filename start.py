from threading import Thread
import signal
import RPi.GPIO as GPIO
from time import sleep

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
    
    sleep(5)

    sound.control.text4()

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
    light.control.l7_on()

    motors.m4.init(800)
    T = Thread(target=motors.m4.right, args=[2.25])
    T.start()

    sound.control.lied4()

    motors.m4.init(1000)
    T = Thread(target=motors.m4.left, args=[2.25])
    T.start()

    light.control.l5_off()
    light.control.l7_off()

def szene6():
    light.control.l6_on()
    sound.control.text7()

    motors.m5.init(1000)
    T2 = Thread(target=motors.m5.left, args=[12.5])
    T2.start()

    sleep(15)

    motors.m6.init(1000)
    T0 = Thread(target=motors.m6.right, args=[8.5])
    T0.start()

    sound.control.lied5()

    sleep(5)
    
    light.control.l6_off()

    motors.m6.init(1000)
    T2 = Thread(target=motors.m6.left, args=[8.5])
    T2.start()

    motors.m5.init(1000)
    motors.m5.right(12.5)

    motors.m5.stop()
    motors.m6.stop()
    sleep(5)

    
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


def main():
    try:
        licht_off()
        sleep(5)
        intro()
        szene1()
        szene2()
        szene3()
        szene4()
        sleep(3)
        szene5()
        szene6()

        sleep(15)
        licht_on()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
