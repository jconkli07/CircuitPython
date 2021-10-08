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
<img src="https://github.com/jconkli07/CircuitPython/blob/af79cffc5f3bd86c43225dd5d83688da25afce92/Files/distance_sensor.gif" width="25%" height="25%"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/8eb1d31a7b16f5f39595933d09eee7c5872549c2/Files/distance_sensor_wiring.png" width="25%" height="25%"/>

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
<img src="https://github.com/jconkli07/CircuitPython/blob/f3b06030b189e906cf269fa30414013dc1e97042/Files/photointerrupter.gif" width="25%" height="25%"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/7cb2f765f1fe9c35ad9e4fabf7c335f3b1d86759/Files/photointerrupter_wiring.png" width="25%" height="25%"/>

### Reflection


## CircuitPython_LCD

### Description & Code

```python
#Jay Conklin
#Displays a count on the LCD that increases once every time a wire is touched.
#If a different wire is touched it changes it to counting down instead of up, or vice versa.
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import touchio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch_a5 = board.A5
touch_A5 = touchio.TouchIn(touch_a5)
touch_a0 = board.A0
touch_A0 = touchio.TouchIn(touch_a0)

count = 0
updown=1

while True:
    if touch_A5.value:
        count+=updown
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))
        while touch_A5.value:
            time.sleep(.01)

    if touch_A0.value:
        updown=-updown
        while touch_A0.value:
            time.sleep(.1)
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/113ffd12f4a13388e2e827ff222791c589bd1f18/Files/lcd.gif" width="25%" height="25%"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/7cb2f765f1fe9c35ad9e4fabf7c335f3b1d86759/Files/photointerrupter_wiring.png" width="25%" height="25%"/>

### Reflection
