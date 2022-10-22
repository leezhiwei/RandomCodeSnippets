while (true) // loop for input prompt
{
    Console.Write("Enter a number: "); // user input prompt
    string input = Console.ReadLine(); // read user input
    double inputdouble; // init double variable
    try // try convert to double
    {
        inputdouble = Convert.ToDouble(input);
    }
    catch // if cannot
    {
        Console.WriteLine("Please enter a number."); // print error
        continue; // continue loop
    }
    for (int x = 1; x <= 12; x++) // for loop, start with 1, end with 12, increment 1
    {
        Console.WriteLine($"{x}: {x * inputdouble}"); // writeline with placeholders
    }
    break; // break loop
}