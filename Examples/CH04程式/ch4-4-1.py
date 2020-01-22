# 圖示閃爍
from microbit import *
def function1():
    display.show(Image.HEART)
    sleep(1000)
    display.show(Image.HEART_SMALL)
    sleep(1000)
    display.show(Image.DIAMOND)
    sleep(1000)
    display.show(Image.DIAMOND_SMALL)
    sleep(1000)

while True:
    if button_a.was_pressed():
        function1()
        display.show('A')
    if button_b.was_pressed():
        function1()
        display.show('B')