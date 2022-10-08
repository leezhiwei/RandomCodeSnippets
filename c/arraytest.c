#include <stdio.h>
#include <stdint.h>

int checkarr(int *x, int *y, size_t n){ // function to check array
    size_t i = 0; // new var i
    while(x[i] == y[i] && i < n) i ++; // while loop when element is the same and i is less than n (number of elements), increment i.
    return (i == n); // return whether i is equals to n.
}
void main() {
    int mark[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100}; // array test
    const int size = sizeof(mark)/sizeof(mark[0]); //size of array from https://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c
    int mark2[size]; // new array
    printf("Size of array is %d\n",size); //print size of array
    int total = 0; // init total value
    int div = 0; // init division value
    for(int i = 0; i < size; i++){ // for loop to iterate through array
        total += mark[i]; // add current index to total number
        mark2[i] += mark[i]; // add new element to array
        printf("Individual element for mark array is %d\n", mark[i]); // print individual element
        printf("Individual element for mark2 array is %d\n",mark2[i]); // double check the number is written
        printf("I is %d\n", i); // shows current number of I
        printf("Total is %d\n",total); // print total numbers
        if(i == 0){ // divide total by index number, if index is 0.
            div = 0; // make div 0
        }
        else{ // else
            div = total / i; // div is total divided by i 
        }
        printf("Total Divide by i is %d\n", div); // print out div value
    }
    printf("Is mark1 and mark2 array the same? %d\n", checkarr(mark,mark2,size)); // check if both arrays are equal using the functions above.
}
