#include <stdio.h>
#include <math.h>

void menus(int c){ 
    if (c == 1){
        printf("Welcome to Calculator\n ");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Division\n");
        printf("4. Multiplication\n");
        printf("Select your option: ");
    }
    else if (c == 2){
        printf("Please type in the first number: ");
    }
    else if (c == 3){
        printf("Please type in the second number: ");
    }
    else{
        printf("Check function input.");
    }
}
int main() {
    // Write C code here
    int c1;
    long double n1;
    long double n2;
    long double result;
    menus(1);
    scanf("%d",&c1);
    if (c1 == 1){
        menus(2);
        scanf("%Lf",&n1);
        menus(3);
        scanf("%Lf",&n2);
        result = n1 + n2;
        printf("The result is %Lf", result);
    }
    else if (c1 == 2){
        menus(2);
        scanf("%Lf",&n1);
        menus(3);
        scanf("%Lf",&n2);
        result = n1 - n2;
        printf("The result is %Lf", result);
    }
    else if (c1 == 3){
        menus(2);
        scanf("%Lf",&n1);
        menus(3);
        scanf("%Lf",&n2);
        result = n1 / n2;
        printf("The result is %Lf", result);
    }
    else if (c1 == 4){
        menus(2);
        scanf("%Lf",&n1);
        menus(3);
        scanf("%Lf",&n2);
        result = n1 * n2;
        printf("The result is %Lf", result);
    }
    else{
        printf("Invalid input");
    }
    return 0;
}
