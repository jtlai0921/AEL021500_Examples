# Add your Python code here. E.g.
from microbit import *
display.show(Image.ARROW_N)
while True:
    if button_a.was_pressed():
        display.show(Image.ARROW_N.shift_left(1))
    if button_b.was_pressed():
        display.show(Image.ARROW_N.shift_right(1))
    if button_a.was_pressed and button_b.was_pressed():
        display.show(Image.ARROW_N)


