import RPi.GPIO as gpio
import time

LED_PIN = 27
BUTTON_PIN = 17

gpio.setmode(gpio.BCM)
gpio.setup(LED_PIN, gpio.OUT)
gpio.setup(BUTTON_PIN, gpio.IN)

try:

    while True:
        if gpio.input(BUTTON_PIN) == gpio.HIGH:
            gpio.output(LED_PIN, gpio.HIGH)
        else:
            gpio.output(LED_PIN, gpio.LOW)
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    gpio.cleanup()
    print("GPIO cleaned up")