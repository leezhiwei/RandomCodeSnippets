#!/usr/bin/python3
import math
for x in range(1,99**4):
    print(f'X is {x}')
    y = x ** 2
    print(f'Y is {y}')
    z = y ** 9
    print(f'Z is {z}')
    a = math.pi * z
    print(f'A is {a}')
    b = a // x
    print(f'B is {b}')
    c = a % x
    print(f'C is {c}')
