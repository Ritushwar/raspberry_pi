from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

try:
    while True:
        # Fade in
        for i in range(101):
            led.value = i/100
            sleep(0.01)
        
        # Fade Out
        for i in range(100, -1, -1):
            led.value = i/100
            sleep(0.01)
except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    gpio.cleanup()
    print("GPIO cleaned up")