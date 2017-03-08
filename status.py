#!/usr/bin/env python

import time
from random import randint

import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(.4)


#unicorn.set_pixel(x,y,0,150,0)
#unicorn.show()
#time.sleep(5)

while True:
    unicorn.set_pixel(randint(0,7),randint(0,7),randint(100,150),randint(100,200),randint(150,200))
    unicorn.show()
    time.sleep(.05)
