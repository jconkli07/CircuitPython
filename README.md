# CircuitPython

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Distance_Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython_Photointerrupter](#CircuitPython_Photointerrupter)
* [CircuitPython_LCD](#CircuitPython_LCD)
---

## Hello_CircuitPython

### Description & Code

Description goes here

```python

#Jay Conklin
#Makes the LED blink red and blue
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

dot.brightness = 0.1

while True:
    dot.fill((255, 0, 0))
    time.sleep(.5)
    dot.fill((0, 0, 255))
    time.sleep(.5)

```


### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/bc8618933dd1df674c97ab04eacac412698359b3/Files/led%20blink.gif" width="25%" height="25%"/>

### Wiring
Nothing needed except for Neopixel board.

### Reflection

This was a pretty easy assignment for me, I found the code on the internet and modified it a little bit. I had some issues with learning how to save the files and make them run on the board but I figured them out by asking my classmates.

## CircuitPython_Servo

### Description & Code

```python

# Jay Conklin
# Makes a servo rotate 180 degrees
import time
import board
import pwmio
import servo
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/5e9450a07326bc7dca9aa972ea3f7279d5cec847/Files/servo.gif" width="25%" height="25%"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/f851906ed627ad6e53e44df6a1b489bf18236723/Files/servo%20wiring.png" width="25%" height="25%"/>

### Reflection

This assignment was a bit harder than the first one. I looked up the code and the wiring, but I think that next time I could do it myself. I had an issue with the wires being in the same pin as the code said they were in, but I used the feedback on the serial monitor to identify the problem.

## CircuitPython_Distance_Sensor

### Description & Code

```python
# Jay Conklin
# Makes the built-in LED change colors based on how far an object is from the distance sensor.
import adafruit_hcsr04
import time
import board
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = 0.1

while True:
    try:
        dist = sonar.distance
        print((dist))
        r = max(min(17*(20-dist),255),0)
        g = max(min(17*(dist-20),255),0)
        b = max(min(-abs(17*(20-dist))+225,255),0)
        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence

### Wiring

### Reflection


## CircuitPython_Photointerrupter

### Description & Code

```python
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
```

### Evidence

### Wiring

### Reflection


## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
