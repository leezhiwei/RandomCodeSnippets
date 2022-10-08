#!/usr/bin/python3
import math
for x in range(1,99**9):
    y = x ** 2
    z = y ** 5
    a = z * math.pi
    b = a // x
    c = a % x
    print(x,y,z,a,b,c)

