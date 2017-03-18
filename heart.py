#!/usr/bin/env python

import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(90)
unicorn.brightness(.4)
time_sleep = 30

heart=[[0,0,0,1,1,0,0,0],[0,0,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0]]



alpha_array = [heart]

for letter in range(0,52):
	array = alpha_array[letter]
	for row in range(0,8):
		for column in range(len(array[0])):          
                	unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 10, array[row][column] * 10)
	unicorn.show()
	time.sleep(time_sleep)
		    
