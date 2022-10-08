def isprime(number): # isprime fn
    if number == 1 or number == 0: # if 1 or 0 
        return False # return false
    elif number > 1: # if more than 1
        for i in range(2,number): # for loop in range of 2 and num
            if number % i == 0: # if divide and have remainder
                return False # return false
        return True # if for loop completes, return true
for x in range(500): # run for loop from 0 to 500
    if isprime(x) == True: # if function return true
        print(f'{x} is prime') # print the number is prime
    elif isprime(x) == False: # else function return false
        print(f'{x} is not prime') # print number is not prime
    else: # exception catching
        print("Check function output.") # print error
        break # break loop
