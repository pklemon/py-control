import motors.m1
import RPi.GPIO as GPIO
import signal

motors.m1.init(100)
motors.m1.right(1)
motors.m1.stop()



def main():
    setup_gpio()
    try:
        signal.pause()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
