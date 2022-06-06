# CircuitPython

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Distance_Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython_Photointerrupter](#CircuitPython_Photointerrupter)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Fun with RGB LEDs](#Fun_with_RGB_LEDs)
---

## Hello_CircuitPython

### Description & Code
This assignment was to make the LED on the neopixel flash different colors, I chose red and blue. The goal was to get used to the MetroExpress and creating/running code on Mu. Also you learn some about the basics of Circuit python like importing libraries.

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
    time.sleep(.5)  #Wait 1/2 second
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
This assignment was to make a servo roatate 180 degrees, and then back 180 degrees, and have it repeat. This assignment teaches how to wire, code, and operate a servo with the metro express. Also more advanced programming concepts like for loops are used.

```python
# Jay Conklin
# Makes a servo rotate 180 degrees
import time
import board
import pwmio
import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)                 #Sets up servo and pins

while True:
    for angle in range(0, 180, 5):      #Turns servo from 0 to 180 at rate of change 5
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):     #Turns servo from 180 to 0 at rate of change 5
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/5e9450a07326bc7dca9aa972ea3f7279d5cec847/Files/servo.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/62241d3f26ff94e50bd7a05ae380ea1cb6ca0399/Files/servo_wiring.png"/>

### Reflection

This assignment was a bit harder than the first one. I need to make sure that the wires are in the pin that the code says they are in. The errors on the serial monitor are helpful for debugging the code. for loops are used to repeat a chunk of code a certain mount of times.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_Distance_Sensor

### Description & Code
The assignment was to make an LED shift from red to blue to green as an object got further away from a distance sensor. The distance sensor shoots out ultrasonic waves and uses how they have changed when they bounce back (intensity, time to return, etc) to determine the distance from an object. This assignment teaches how to wire and use distance senors. Also it dives into more advanced python with a lot of mathematical operators and variables. It builds on what we learned in the first assignment about changing the color of the LED.

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
        dist = sonar.distance   #Gets the distance and assigns it to the dist variable
        print((dist))
        
                                        #Max and min take the maximum/minimum of the 2 numbers given,
                                        #they make sure that the output value won't be >255 or <0
        r = max(min(17*(20-dist),255),0)    #Makes the red value change from 255-0 as the distance goes from 5-20
        g = max(min(17*(dist-20),255),0)    #Makes the green value change from 0-255 as the distance goes from 20-35
        b = max(min(-abs(17*(20-dist))+255,255),0)  #Makes the blue value change go from 0-255 as the distance goes from 0-20
                                                    #and then makes it go back from 255-0 as the distance goes from 20-35
        dot.fill((int(r), int(g), int(b)))  #Makes the LED flash the predetermined RGB values
                                            #and converts the rgb values into ints because it requires int inputs
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/af79cffc5f3bd86c43225dd5d83688da25afce92/Files/distance_sensor.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/62241d3f26ff94e50bd7a05ae380ea1cb6ca0399/Files/distance_sensor_wiring.png"/>

### Reflection
<a href="https://www.desmos.com/calculator/2clk5c78xj">Link to Desmos graph modeling rbg change</a>  
I had some issues because you cannot use float values in dot.fill() so it was giving me errors. max(x,y) outputs whichever number is highest, min(x,y) does opposite. I used max and min to constrain the rgb values to 0<x<255. I was able to reuse much of the code from the LED blink assignment, and then just add the distance sensor part. int(x) outputs x converted to an integer (it drops any decimals, for example 4.15 becomes 4). I partially simplified the equations so things like 255(20-dist)/15 became 17(20-dist). abs(x) returns the absolute value of the number, I used this to make the blue value increase and then decrease.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_Photointerrupter

### Description & Code
The assignment was to make code that would detect the number of times the photointerrupter has sensed an interrupt and display this count every 4 seconds. I used time.monotonic() to know when 4 seconds passed. This taught me about if statements and how to code for the photoresistor.

```python
#Jay Conklin
#Counts up the photointerrupter interruptions and displays the count every 4 seconds

import digitalio
import time
import board
from digitalio import DigitalInOut, Direction, Pull

interrupter = DigitalInOut(board.D2)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP                  #Sets up photoresistor and pins
initial = time.monotonic()

counter = 0

photo = False
state = False

start=time.monotonic()      #Starts the "clock" which will run for as long as the program continues

while True:
    photo=interrupter.value
    if photo and not state:
        counter+=1
    state = photo           #Above code checks for interrupts and increase counter by 1 each time there is one
    
    math = time.monotonic()/4
    if math==int(math):     #Takes the total amount of time the program has ran (in secs) and divides it by 4
                            #Then it takes that number and checks if chopping all of the decimals off will change the number
                            #If the numbers are equal it means that the number of seconds elapsed have been a multiple of 4
        print("The number of Interrupts is ", str(counter))
        time.sleep(.001)
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/5c7f11c6d55d759477bea77de701069a4c99ec07/Files/photointerrupter.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/62241d3f26ff94e50bd7a05ae380ea1cb6ca0399/Files/photointerrupter_wiring.png"/>

### Reflection
I used digitalio to sense the number of interrupts from the photointerrupter. x==y CHECKS whether x=y and returns true of false, x=y sets x equal to y. variable+=x sets variable equal to variable+x. time.monotonic starts counting and then doesn't stop, I used to to determine when 4 seconds had passed. DO NOT LET THE + OR L WIRES TOUCH THE OUT WIRE IT WILL FRY THE PHOTORESISTOR. Use electrical tape to prevent it.

[Back to Table of Contents](#Table-of-Contents)

## CircuitPython_LCD

### Description & Code
The assignment is to have an LCD display a count that chages by 1 each time a wire is touched. Each time another wire is touched the direction in which it is counting switches. I used capacitative touch to sense when the wires were touched. I learned how to code capacitative touh and the LCD. This teaches how to manage and debug more complicated and longer code.

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
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)      #Sets up the lcd board and tells code what pins it's in

touch_a5 = board.A5
touch_A5 = touchio.TouchIn(touch_a5)    #Sets up capacitative touch for the counter wire
touch_a0 = board.A0
touch_A0 = touchio.TouchIn(touch_a0)    #Sets up capacitative touch for the up/down wire

count = 0
updown=1

while True:
    if touch_A5.value:
        count+=updown   #If counter wire is touched adds updown variable to the counter number
                        #Updown will be 1 if going up or -1 if going down, so just adding
                        #it to the counter will make it count 1 in the correct direction
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))   #Above section displays direction of counting and new count
        while touch_A5.value:   #Waits until the wire is released to continue
            time.sleep(.01)     #that holding down the wire does not increase the number over and over

    if touch_A0.value:
        updown=-updown          #If direction wire touched changes updown from 1 to -1 or vice versa
        while touch_A0.value:
            time.sleep(.1)
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))   #Above section displays the new direction of counting and current count (the count stays the same)
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/113ffd12f4a13388e2e827ff222791c589bd1f18/Files/lcd.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/62241d3f26ff94e50bd7a05ae380ea1cb6ca0399/Files/lcd_wiring.png"/>

### Reflection
Capacitative touch can sense when you touch a wire. I used lcd.print(str(count)) to print the value of a variable set to a number. lcd.clear() clears lcd. "if touchio.TouchIn(board.A5).value:" will run if the wire in that pin is touched. 

[Back to Table of Contents](#Table-of-Contents)

## Fun_with_RGB_LEDs

### Description & Code
The assignment is to make 2 rgb LEDs blink, change colors, and do other actions. I achieved this through the use of classes, objects and moduels. This is the first assignment where we have dealt with these things, so I learned a lot about them from this.

main.py code:
```python
#From Lucy Gray
import time
import board
from rgb import RGB

redLEDPin1 = board.D10
greenLEDPin1 = board.D9
blueLEDPin1 = board.D8

redLEDPin2 = board.D7
greenLEDPin2 = board.D5
blueLEDPin2 = board.D4  #D6 is using the same timer as D8,9,10.  Avoid!

full = 65535
half = (65535/5)

myRGBled1 = RGB(redLEDPin1, greenLEDPin1, blueLEDPin1)
myRGBled2 = RGB(redLEDPin2, greenLEDPin2, blueLEDPin2)


while True:
''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import RGB

redLEDPin1 = board.D10
greenLEDPin1 = board.D9
blueLEDPin1 = board.D8

redLEDPin2 = board.D7
greenLEDPin2 = board.D5
blueLEDPin2 = board.D4  #D6 is using the same timer as D8,9,10.  Avoid!

full = int(65535)
half = int(65535/2)

myRGBled1 = RGB(redLEDPin1, greenLEDPin1, blueLEDPin1)
myRGBled2 = RGB(redLEDPin2, greenLEDPin2, blueLEDPin2)


while True:
    myRGBled1.blue()
    myRGBled2.yellow()
    time.sleep(1)
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.green(half)
    myRGBled2.magenta(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.white(half)
    myRGBled2.white(half)
    time.sleep(.25)
    myRGBled1.white()
    myRGBled2.white()
    time.sleep(.25)
    myRGBled1.white(half)
    myRGBled2.white(half)
    time.sleep(.25)
    myRGBled1.white()
    myRGBled2.white()
    time.sleep(.25)
    myRGBled1.white(half)
    myRGBled2.white(half)
    time.sleep(.25)
    myRGBled1.white()
    myRGBled2.white()
    time.sleep(.25)
    myRGBled1.white(half)
    myRGBled2.white(half)
    time.sleep(.25)
    myRGBled1.white()
    myRGBled2.white()
    time.sleep(.25)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(5)

# extra spicy (optional) part
# you should replace "rate1" with a real number...
    myRGBled1.rainbow(2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
    myRGBled2.rainbow(.5) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
    time.sleep(5)
```

rgb.py code:
```python
#From Lucy Gray
import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness  # these are reversed!!! 
        # rgb leds pull current the opposite way as you would expect
        lightBulb.value = 65535


    def off(self): # "off" means duty cycle should be full.
        self.led.duty_cycle = 65535


class RGB:
    '''this class should impliment all 3 pins together to control an RGB LED - up until here is Mr. H's'''
    from rgb import LED  # use methods set up in led, like on, off

    def __init__(self, redPin, greenPin, bluePin):
        self.myRedLED = LED(redPin, "red")  # initialise ledpins using class LED
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def blue(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)  # using brightness, otherwise it won't change
        self.myGreenLED.off()
        self.myRedLED.off()

    def yellow(self, brightness=65535):
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)  # yes, yellow is green and red. gross
        self.myRedLED.on(brightness)

    def red(self, brightness=65535):
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def cyan(self, brightness=65535):
        self.myBlueLED.on(brightness)  # color theory
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def green(self, brightness=65535):
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def magenta(self, brightness=65535):
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def white(self, brightness=65535):
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)
    
    def rainbow(self, rate):
        self.myBlueLED.off()  # red
        self.myGreenLED.off()
        self.myRedLED.on()
        time.sleep(rate)  # time sleep value equal to the rate defined in main
        self.myBlueLED.off()  # yellow
        self.myGreenLED.on()
        self.myRedLED.on()
        time.sleep(rate)
        self.myBlueLED.off()  # green
        self.myGreenLED.on()
        self.myRedLED.off()
        time.sleep(rate)
        self.myBlueLED.on()
        self.myGreenLED.on()  # cyan
        self.myRedLED.off()
        time.sleep(rate)
        self.myBlueLED.on()  # blue
        self.myGreenLED.off()
        self.myRedLED.off()
        time.sleep(rate)
        self.myBlueLED.on()  # magenta
        self.myGreenLED.off()
        self.myRedLED.on()
        time.sleep(rate)
        self.myBlueLED.on()  # white
        self.myGreenLED.on()
        self.myRedLED.on()
        time.sleep(rate)


    def off(self):
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0
```

### Evidence
<img src="https://github.com/jconkli07/CircuitPython/blob/113ffd12f4a13388e2e827ff222791c589bd1f18/Files/lcd.gif"/>

### Wiring
<img src="https://github.com/jconkli07/CircuitPython/blob/4b8832a3ba7e4f7e45fb653fc2c6664be54c6461/Files/rgb_wiring.jpeg"/>

### Reflection
This assignment was very useful and I feel that I learned a lot about Circuit Python from it. A module is somethinhg that is imported, at the top of the code, and adds additional functions/commands to Circuit Python. A class is like creating your own custom module. You can determine special commands, traits, and other things about it. An object is an instance of a class with specific traits. For example, ther could be a class of Dog with the attributes of color and breed, and an object instance of that class would be Zeke, who is black and a labrador.

[Back to Table of Contents](#Table-of-Contents)
