#!/usr/bin/env python

import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(.4)

A=[[1,1,1,1,1,1,0,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[1,1,1,1,1,1,0,0]]
B=[[1,1,1,1,1,1,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[0,1,1,0,1,1,0,0]]
C=[[0,1,1,1,1,1,0,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[0,1,0,0,0,1,0,0]]
D=[[1,1,1,1,1,1,1,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]]
E=[[1,1,1,1,1,1,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,0,0,0,1,0]]
F=[[1,1,1,1,1,1,1,0],[0,0,0,1,0,0,1,0],[0,0,0,1,0,0,1,0],[0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0]]
G=[[0,1,1,1,1,1,0,0],[1,0,0,0,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[1,1,1,1,0,1,0,0]]
H=[[1,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,0]]
I=[[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[1,1,1,1,1,1,1,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0]]
J=[[0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0]]
K=[[1,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,1,0]]
L=[[1,1,1,1,1,1,1,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
M=[[1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0],[1,1,1,1,1,1,1,0]]
N=[[1,1,1,1,1,1,1,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[1,1,1,1,1,1,1,0]]
O=[[0,1,1,1,1,1,0,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]]
P=[[1,1,1,1,1,1,1,0],[0,0,0,1,0,0,1,0],[0,0,0,1,0,0,1,0],[0,0,0,1,0,0,1,0],[0,0,0,0,1,1,0,0]]
Q=[[0,1,1,1,1,1,0,0],[1,0,0,0,0,0,1,0],[1,0,1,0,0,0,1,0],[0,1,0,0,0,0,1,0],[1,0,1,1,1,1,0,0]]
R=[[1,1,1,1,1,1,1,0],[0,0,0,1,0,0,1,0],[0,0,1,1,0,0,1,0],[0,1,0,1,0,0,1,0],[1,0,0,0,1,1,0,0]]
S=[[1,0,0,0,1,1,0,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,1,0,0,1,0],[0,1,1,0,0,0,1,0]]
T=[[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[1,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0]]
U=[[0,1,1,1,1,1,1,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0]]
V=[[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0]]
W=[[0,1,1,1,1,1,1,0],[1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0],[1,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0]]
X=[[1,1,0,0,0,1,1,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[1,1,0,0,0,1,1,0]]
Y=[[0,0,0,0,1,1,1,0],[0,0,0,1,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,1,1,0]]
Z=[[1,1,0,0,0,0,1,0],[1,0,1,0,0,0,1,0],[1,0,0,1,0,0,1,0],[1,0,0,0,1,0,1,0],[1,0,0,0,0,1,1,0]]

array = A

print len(array[0])



for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
                #unicorn.show()
                #time.sleep(.05)
                #print row, " ", column

unicorn.show()
time.sleep(1)

array = B

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = C

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = D

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = E

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = F

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = G

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = H

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = I

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = J

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = K

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = L

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = M

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = N

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = O

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = P

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = Q

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = R

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = S

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = T

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = U

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = V

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = W

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = X

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = Y

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)

array = Z

for row in range(0,5):
	for column in range(len(array[0])):          
                unicorn.set_pixel(row, column, array[row][column] * 255, array[row][column] * 100, array[row][column] * 100)
unicorn.show()
time.sleep(1)