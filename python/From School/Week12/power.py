'''
Power v0.5
Lee Zhi Wei
4/7/22
'''
'''
def power(x,n): # def power fn
    if x !=0:
        import math #import math
        pow = math.pow(x,n) # use pow function
        return pow # return pow value
'''
import time
start = time.time()
def power(x,n):
    res = 1
    for y in range(n):
        res *= x
    return res
x = int(input("Enter base: "))# Enter base
n = int(input("Enter exponent: ")) # enter exponent
print(power(x,n)) # print result
print(time.time() -start)
