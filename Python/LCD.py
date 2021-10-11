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
