#include <stdio.h>
#include <math.h>

int main()
{
	for(long int x = 1; x < pow(99,4); x++){ // for loop 1 to 99 power 4
		printf("X is %Li\n",x); // print x as long int
		long double y = pow(x,2); // y is x power 2
		printf("Y is %Lf\n",y); // print y as long float
		long double z = pow(y,9); // z is y power 9
		printf("Z is %Lf\n",z); // print z as long float
		long double a = 3.14159 * z; // a is pi multiply z
		printf("A is %Lf\n", a); // print a as long floar
		long double tempb = a / x; // temp b is a divide x
		long double b = floor(tempb); // b is tempb floor
		printf("B is %Lf\n",b); // print b as long float
		long double c = fmod(a,x); // c is a modulus x
		printf("C is %Lf\n",c); // print c as long float
	}
}
