#Second day project added 3 LED's and a transistor which were able to respond to the 18,19 and 20 out pins on the Pico H.

from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 0

while counter < 5:
    red.value(1)
    amber.value(0)
    green.value(0)
    
    time.sleep(0.5)
    
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(0.5)

    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(0.5)

    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(0.5)
    
    red.value(0)
    amber.value(1)
    green.value(0)    

    time.sleep(0.5)
    
    counter +=1

