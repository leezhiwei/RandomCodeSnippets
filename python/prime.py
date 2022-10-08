def isprime(number):
    if number == 1 or number == 0:
        return False
    elif number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
for x in range(500):
    if isprime(x) == True:
        print(f'{x} is prime')
    elif isprime(x) == False:
        print(f'{x} is not prime')
    else:
        print("Check function output.")
        break
