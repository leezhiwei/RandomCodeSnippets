import random
import math
for x in range(1,99**9):
    y = x ** 2
    radsq = math.pow(y,6)
    area = math.pi * radsq
    floor = area // x
    mod = area % x
    rand = random.randint(1,radsq)
    print(x,y,radsq,area,floor,mod,rand)
