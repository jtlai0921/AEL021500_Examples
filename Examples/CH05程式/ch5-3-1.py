# Marry Me
from microbit import *
import radio
radio.on()
radio.config(group=20)
while True:
    inputnumber = radio.receive()
    if accelerometer.was_gesture('shake'):
        radio.send("M")
        display.show("Marry Me ?")
    if button_a.was_pressed():
        radio.send("Y")
        display.show("Yes")
    if button_b.was_pressed():
        radio.send("N")
        display.show("No")
    if inputnumber == "M":
        display.show("Marry Me ?")
    if inputnumber == "Y":
        display.show("Yes")
    if inputnumber == "N":
        display.show("No")