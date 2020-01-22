# 碼表計時器
from microbit import *
index = 0
while True:
    if button_a.was_pressed():
        if index == 0:
            display.show(Image.YES)
            index = index + 1
        elif index != 0:
            for x in range(0, 10):
                display.show(x)
                sleep(1000)



