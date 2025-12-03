#little bit of code that can make the LED Blink on the Pico H.

from machine import Pin

MainLED = Pin(25, Pin.OUT)
MainLED.value(0)
