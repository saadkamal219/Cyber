import rotatescreen
from display import *
import time

screen = rotatescreen.get_primary_display()

for i in range(100):
    time.sleep(1)
    screen.rotate_to(1*90 % 360)
