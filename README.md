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
This assignment was to make the LED on the neopixel flash different colors, I chose red and blue.

```python
#Jay Conklin
#Makes the LED blink red and blue
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = 0.1

while True:
    dot.fill((255, 0, 0))   #Turns the light red
    time.sleep(.5)
    dot.fill((0, 0, 255))   #Turns the light blue
    time.sleep(.5)

```


### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/bc8618933dd1df674c97ab04eacac412698359b3/Files/led%20blink.gif"/>

### Wiring
Nothing needed except for Neopixel board.

### Reflection

This was a pretty easy assignment for me, I found the code on the internet and modified it a little bit. I need to only have the main.py saved in the neopixel, the other codes should be saved in a folder on my computer. Saving code runs it on the board. Importing libraries helps to add functionalities, for example importing time allows the program to be able to pause for a set amount of time.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_Servo

### Description & Code
This assignment was to make a servo roatate 180 degrees, and then back 180 degrees, and have it repeat.
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
<img src="https://github.com/jconkli07/CircuitPython/blob/5e9450a07326bc7dca9aa972ea3f7279d5cec847/Files/servo.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/f851906ed627ad6e53e44df6a1b489bf18236723/Files/servo%20wiring.png"/>

### Reflection

This assignment was a bit harder than the first one. I need to make sure that the wires are in the pin that the code says they are in. The errors on the serial monitor are helpful for debugging the code. for loops are used to repeat a chunk of code a certain mount of times.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_Distance_Sensor

### Description & Code
The assignment was to make an LED shift from red to blue to green as an object got further away from a distance sensor.
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
<img src="https://github.com/jconkli07/CircuitPython/blob/af79cffc5f3bd86c43225dd5d83688da25afce92/Files/distance_sensor.gif"/>
<a href="https://www.desmos.com/calculator/oyaopfyd2x">Link to Desmos graph modeling rbg change</a>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/8eb1d31a7b16f5f39595933d09eee7c5872549c2/Files/distance_sensor_wiring.png"/>

### Reflection
I had some issues because you cannot use float values in dot.fill() so it was giving me errors. max(x,y) outputs whichever number is highest, min(x,y) does opposite. I was able to reuse much of the code from the LED blink assignment, and then just add the distance sensor part. int(x) outputs x converted to an integer (it drops any decimals, for example 4.15 becomes 4).

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_Photointerrupter

### Description & Code
The assignment was to make code that would detect the number of times the photointerrupter has sensed an interrupt and display this count every 4 seconds.

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
<img src="https://github.com/jconkli07/CircuitPython/blob/f3b06030b189e906cf269fa30414013dc1e97042/Files/photointerrupter.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/7cb2f765f1fe9c35ad9e4fabf7c335f3b1d86759/Files/photointerrupter_wiring.png"/>

### Reflection
I used digitalio to sense the number of interrupts from the photointerrupter. x==y CHECKS whether x=y and returns true of false, x=y sets x equal to y. variable+=x sets variable equal to variable+x. time.monotonic starts counting and then doesn't stop, I used to to determine when 4 seconds had passed.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_LCD

### Description & Code
The assignment is to have an LCD display a count that chages by 1 each time a wire is touched. Each time another wire is touched the direction in which it is counting switches.

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
<img src="https://github.com/jconkli07/CircuitPython/blob/113ffd12f4a13388e2e827ff222791c589bd1f18/Files/lcd.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/fcf6362f6df3a11c4990f65ba9b9aac7934d2dc5/Files/lcd_wiring.png"/>

### Reflection
Capacitative touch can sense when you touch a wire. I used lcd.print(str(count)) to print the value of a variable set to a number. lcd.clear() clears lcd. "if touchio.TouchIn(board.A5).value:" will run if the wire in that pin is touched. 

[Back to Table of Contents](#Table-of-Contents)
