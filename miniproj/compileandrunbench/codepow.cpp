#include <iostream>
#include <math.h>
int main()
{
	for(long int x = 1; x <= pow(99,4); x++){ // for x in range(1,99*4)
		std::cout << "X is " << x << std::endl; // send x to cout
		long double y = pow(x,2); // y = x ** 2
		std::cout << "Y is " << y << std::endl; // send y to cout
		long double z = pow(x,9); // z = y ** 9
		std::cout << "Z is " << z << std::endl; // send z to cout
		long double a = 3.14159 * z; // a = pi * z
		std::cout << "A is " << a << std::endl; // send a to cout
		long double tempb = a / x; // tempb = a div x
		long double b = floor(tempb); // b = floor tempb
		std::cout << "B is " << b << std::endl; // send b to cout
		long double c = fmod(a,x); // c is a mod x
		std::cout << "C is " << c << std::endl; // send c to cout
	}
}
