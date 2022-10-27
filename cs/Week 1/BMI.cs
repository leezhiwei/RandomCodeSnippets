while (true)
{
    double weightdouble; // init weightdouble variable
    double heightdouble; // init heightdouble variable
    Console.Write("What is your Height (in metres)? "); // prompt for height
    string height = Console.ReadLine(); // get user input and set into var
    try // try this code
    {
        heightdouble = Convert.ToDouble(height); // if can convert
    }
    catch // if cannot
    {
        Console.WriteLine("Please enter a valid input."); // error
        continue; // continue loop
    }
    Console.Write("What is your Weight (in kilograms)? "); // prompt for weight
    string weight = Console.ReadLine(); // get user input and set into var
    try // try this code
    {
        weightdouble = Convert.ToDouble(weight); // if can convert
    }
    catch // if cannot
    {
        Console.WriteLine("Please enter a valid input."); // print error
        continue; // continue loop
    }
    double bmiresult = weightdouble / Math.Pow(heightdouble, 2); ; // calculate bmi via formula.
    Console.WriteLine($"Your BMI is {Math.Round(bmiresult, 2)}"); // print to console
    if (bmiresult < 18.5) // if bmiresult is less than 18.5
    {
        Console.WriteLine("You are underweight."); // print underweight
    }
    else if (18.5 <= bmiresult && bmiresult < 23) // if bmiresult between 18.5 and 23
    {
        Console.WriteLine("You are normal weight. "); // print normal weight
    }
    else if (23 <= bmiresult && bmiresult < 27.5) // if bmiresult between 23 and 27.5
    {
        Console.WriteLine("You are overweight"); // print overweight
    }
    else if (bmiresult > 27.5) // if more than 27.5
    {
        Console.WriteLine("You are obese."); // print obese
    }
    else // else exception catching
        Console.WriteLine("Invalid BMI."); // print invalid
    break; // break loop once the calculation is done
}