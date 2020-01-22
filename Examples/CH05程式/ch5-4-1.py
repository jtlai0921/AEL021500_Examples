from microbit import *

P = Image("22222:"
          "20002:"
          "20002:"
          "20002:"
          "22222")
xx = 2
yy = 2
error = 0
while error == 0 and running_time() < 60000:
    display.show(P)
    if button_a.was_pressed():
        xx = (xx+1) % 5
    elif button_b.was_pressed():
        yy = (yy+1) % 5
    elif accelerometer.was_gesture("shake"):
        xx = (xx-1) % 5
    elif button_a.was_pressed() and button_b.was_pressed():
        yy = (yy-1) % 5
    if display.get_pixel(xx, yy) != 2:
        display.set_pixel(xx, yy, 9)
    else:
        error = 1

if error == 0:
    display.scroll('winner!'+str(running_time()/1000) + 's', loop=True)
else:
    display.show(Image.NO)
    sleep(500)
    display.scroll('GameOver!'+str(running_time()/1000) + 's', loop=True)