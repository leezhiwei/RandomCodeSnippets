using System;

public class HelloWorld
{
    static bool isprime(int number){
        if (number == 1 || number == 0){
            return false;
        }
        else if (number >= 2){
            for (int x = 2; x < number; x++){
                if (number % x == 0){
                    return false;
                }
            }
            return true;
        }
        else{
            return false;
        }
    }
    public static void Main(string[] args)
    {
        for (int x = 0; x <= 500; x++){
            if (isprime(x) == true){
                Console.WriteLine($"{x} is prime");
            }
            else if (isprime(x) == false){
                Console.WriteLine($"{x} is not prime");
            }
            else {
                Console.WriteLine("Check output of function.");
                break;
            }
        }
    }
}
