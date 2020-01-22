# 點往高處跑
from microbit import *
x = 2
y = 2
display.set_pixel(x, y, 9)
while True:
    ax = accelerometer.get_x()
    ay = accelerometer.get_y()
    if ax > 200 and x > 0:
        x = x - 1
    if ax < -200 and x < 4:
        x = x + 1
    if ay > 200 and y > 0:
        y = y - 1
    if ay < -200 and y < 4:
        y = y + 1
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(500)