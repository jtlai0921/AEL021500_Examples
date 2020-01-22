# Add your Python code here. E.g.
from microbit import *
while True:
    if button_a.was_pressed():
        display.show('Good morning!')
    if button_b.was_pressed():
        display.show(len('Good morning!'))
    if accelerometer.was_gesture("shake"):
        display.show(str('Good morning!'[5:12:1]))

