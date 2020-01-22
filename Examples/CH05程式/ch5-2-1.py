# 兩隻老虎
from microbit import *
import music
def Tiger_1():
    tune = ["C4:4", "D4:4", "E4:4", "C4:4"]
    music.play(tune)
def Tiger_2():
    tune = ["E4:4", "F4:4", "G4:8"]
    music.play(tune)
while True:
    if button_a.was_pressed():
        display.show('Tiger')
        Tiger_1()
        Tiger_1()
        Tiger_2()
        Tiger_2()