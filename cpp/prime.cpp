#include <iostream>
bool isprime(int number){ // isprime fn
    if (number == 0 || number == 1){ // if 0 or 1
        return false; // return false
    }
    else if (number >= 2){ // if num more than 2
        for (int x = 2; x < number; x++){ // for x in range (2,number)
            if (number % x == 0){ // if number mod 2 = 0, eg no remainder, result is whole
                return false; // return false
            }
        }
        return true; // if can continue loop, return true
    }
}
int main() { // main fn
    for(int x = 0; x < 500; x++){ // for x in range(0,500)
        if (isprime(x) == true){ // if isprime fn is true
            std::cout << x << " is prime." << std::endl; // print success message to cout
        }
        else if (isprime(x) == false){ // else if fn is false
            std:: cout << x << " is not prime." << std::endl; // print false msg
        }
        else{ // exception catching
            std::cout << "Check the output of the function." << std::endl; // if output not expected
            break; // break loop
        }
    }
    return 0; // return 0 once ended
}
