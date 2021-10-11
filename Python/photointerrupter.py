#Jay Conklin
#Counts up the photointerrupter interruptions and displays the count every 4 seconds

import digitalio
import time
import board
from digitalio import DigitalInOut, Direction, Pull

interrupter = DigitalInOut(board.D2)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP
initial = time.monotonic()

counter = 0

photo = False
state = False

start=time.monotonic()

while True:
    photo=interrupter.value
    if photo and not state:
        counter+=1
    state = photo
    
    math = time.monotonic()/4
    if math-int(math)==0:
        print("The number of Interrupts is ", str(counter))
        time.sleep(.001)
