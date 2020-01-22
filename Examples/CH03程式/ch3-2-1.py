from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Hello!")
    else:
        display.show(Image.NO)