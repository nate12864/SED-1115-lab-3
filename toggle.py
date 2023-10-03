from machine import pin
import time

sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(18, Pin.OUT)
buttonpushed = False
laststate = False

buttonstate = sw5.value()
if not buttonstate:
    time.sleep(0.02)
#test github