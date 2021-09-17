# CircuitPython

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
