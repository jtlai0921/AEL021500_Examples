# Add your Python code here. E.g.
from microbit import *
x = 0
display.show(0)
while True:
    if button_a.was_pressed():
        display.show(x+1)
        x = x+1
    if button_b.was_pressed():
        display.show(0)
        x = 0


