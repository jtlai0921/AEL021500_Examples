#當按下A鍵出現心跳3次的範例
from microbit import *
display.show(Image.HEART)
while True:
    if button_a.was_pressed():
        for x in range (3):
            display.show(Image.HEART)
            sleep(1000)
            display.show(Image.HEART_SMALL)
            sleep(1000)
        display.clear()