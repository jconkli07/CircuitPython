#Jay Conklin
#Makes the LED blink red and blue
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = 0.1

while True:
    dot.fill((255, 0, 0))
    print("Make it red!!!")
    time.sleep(.5)
    dot.fill((0, 0, 255))
    print("Make it blue!!!")
    time.sleep(.5)
    
