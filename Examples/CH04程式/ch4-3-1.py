# 終極密碼
from microbit import *
import random
X = random.randint(0, 10)
Y = 0
display.show(Image.HAPPY)
while True:
    if button_a.was_pressed():
        Y = Y + 1
        display.show(Y)
        if Y > 10:
            Y = 0
            display.show(Y)
    if button_b.was_pressed():
        Y = Y - 1
        display.show(Y)
        if Y <= 0:
            Y = 0
            display.show(Y)
    while (X == Y):
        display.show(str('Bingo!' + 'New Game'))
        Y = 0
        display.show(Image.HAPPY)