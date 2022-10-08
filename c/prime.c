#include <stdio.h>
#include <stdbool.h>

bool isprime(int num){ // prime number function
	bool prime = true; // set init value
	if (num == 1 || num == 0 || num == 4 ){ // if 1 or 0 or 4
		return false;} // make it false
	else if (num == 2 || num == 3){ // if 2 or 3
		return true;} // return true
	else{ // else 
		for (int tempval = 2; tempval <= num / 2; ++tempval){ // for loop init value 2, less than num divided 2
			if (num % tempval == 0){ // if number divided by loop value has no remainder (basically get whole no)
				prime = false; // prime is false
				break; // break the loop
				}
			else {
				prime = true; // else not divisible, make it true
				}	
		}
}
	return prime; // return bool value
}
int main(){ // main fn
	for (long int x = 0; x <= 99999999999999999999999999999999; x++){ // for x in range of 0 and 999...
		if (isprime(x) == false){ // run the fn with the x value, if false
			printf("%Li is not prime\n",x); // print false statement
			}
		else if (isprime(x) == true){ // run fn, if true
			printf("%Li is prime\n",x); // print true statement
			}
		else { // exception catching
			printf("Check function output"); // show error
			break; // break
			}
	}
	return 0; // return 0, cause int fn
}	
