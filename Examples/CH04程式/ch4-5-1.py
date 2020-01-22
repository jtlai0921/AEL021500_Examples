# 餐食選擇
from microbit import *
import random
meal = ['Rice', 'Noodles', 'Pizza']
display.show(Image.HAPPY)

while True:
    if accelerometer.was_gesture('shake'):
        sleep(100)
        display.scroll(random.choice(meal))
        display.show(Image.HAPPY)