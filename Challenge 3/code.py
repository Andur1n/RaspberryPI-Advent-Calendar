#code adapted for the items of challenge 3 today which added an extra breadboard with buttons. The code below allows the buttons to turn the lights on and off.

from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:

    time.sleep(0.5) #
            
    if button1.value() == 1: 
        
        print("Button 1 pressed")
        
        red.toggle() 
        
    elif button2.value() == 1:
        
        print("Button 2 pressed")
        
        amber.toggle()
    
    elif button3.value() == 1:
        
        print("Button 3 pressed")
        
        green.toggle()
        

