#!/usr/bin/python3
import math # import math
for x in range(1,99**4): # for loop 1 and 99 pow 4
    print(f'X is {x}') # print x 
    y = x ** 2 # y is x squared
    print(f'Y is {y}') # print y
    z = y ** 9 # z is y power 9
    print(f'Z is {z}') # print z
    a = math.pi * z # a is pi * z
    print(f'A is {a}') # print a
    b = a // x # b is a floor x
    print(f'B is {b}') # print b
    c = a % x # c is a mod x
    print(f'C is {c}') # print c
