void menu() // menu fn
{
    Console.WriteLine("------------- MENU --------------");
    Console.WriteLine("[1] Calculate Body Mass Index");
    Console.WriteLine("[2] Calculate Discount");  // print menu
    Console.WriteLine("[3] Display Multiplication Table");
    Console.WriteLine("[0] Exit");
    Console.WriteLine("---------------------------------");
    Console.Write("Enter your option: ");
}
while (true) // infinite while loop
{
    menu(); // run fn
    string userinput = Console.ReadLine(); // get user input as string
    int input; // set initial input as an int
    try // try catch for alpha
    {
        input = Convert.ToInt32(userinput); // if unable to do this
    }
    catch (Exception e) // do something
    {
        Console.WriteLine("Please enter a number."); // print this error
        Console.WriteLine($"Exception thrown is {e.Message}");
        continue; // continue loop
    }
    if (input == 1)
    {
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
            catch (Exception e) // if cannot
            {
                Console.WriteLine("Please enter a valid input."); // error
                Console.WriteLine($"Exception thrown is {e.Message}");
                continue; // continue loop
            }
            Console.Write("What is your Weight (in kilograms)? "); // prompt for weight
            string weight = Console.ReadLine(); // get user input and set into var
            try // try this code
            {
                weightdouble = Convert.ToDouble(weight); // if can convert
            }
            catch (Exception e) // if cannot
            {
                Console.WriteLine("Please enter a valid input."); // print error
                Console.WriteLine($"Exception thrown is {e.Message}");
                continue; // continue loop
            }
            double bmiresult = weightdouble / Math.Pow(heightdouble, 2); ; // calculate bmi via formula.
            try
            {
                if (bmiresult <= 0)
                {
                    throw new Exception("Cannot have negative BMI.");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                break;
            }
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
    }
    else if (input == 2)
    {
        while (true) // loop for input prompt
        {
            Console.Write("Enter amount in dollars: "); // user input prompt
            string price = Console.ReadLine(); // convert user input to double
            double pricedouble;
            try
            {
                pricedouble = Convert.ToDouble(price);
            }
            catch (Exception e)
            {
                Console.WriteLine("Please input a number.");
                Console.WriteLine($"Exception thrown is {e.Message}");
                continue;
            }
            int disrate; // init disrate variable
            if (pricedouble <= 100) // if price is less than or equal to 100
            {
                disrate = 0; // no disrate
            }
            else if (100 < pricedouble && pricedouble <= 500) // if between 100 and 500
            {
                disrate = 5; // disrate is 5
            }
            else if (500 < pricedouble && pricedouble <= 1000) // if within 500 to 1000
            {
                disrate = 10; // disrate is 10
            }
            else if (pricedouble > 1000) // if more than 1000
            {
                disrate = 20; // disrate is 20
            }
            else // else (error catching)
            {
                disrate = 0; // set default to 0
            }
            Console.WriteLine($"The discount rate is : {disrate}%"); // print discount rate in percent
            double discountedprice = pricedouble * ((double)disrate / 100); // calculate price, convert disrate to double
            Console.WriteLine($"The discounted price is : ${discountedprice:F2}"); // print discounted rate to 2 floating point
            break; // break the loop
        }
    }
    else if (input == 3)
    {
        while (true) // loop for input prompt
        {
            Console.Write("Enter a number: "); // user input prompt
            string number = Console.ReadLine(); // read user input
            double inputdouble; // init double variable
            try // try convert to double
            {
                inputdouble = Convert.ToDouble(number);
            }
            catch (Exception e) // if cannot
            {
                Console.WriteLine("Please enter a number."); // print error
                Console.WriteLine($"Exception thrown is {e.Message}");
                continue; // continue loop
            }
            for (int x = 1; x <= 12; x++) // for loop, start with 1, end with 12, increment 1
            {
                Console.WriteLine($"{x}: {x * inputdouble}"); // writeline with placeholders
            }
            break; // break loop
        }
    }
    else if (input == 0) // if option to exit
    {
        break; // break out of infinite loop
    }
    else // if not number
    {
        Console.WriteLine("Please input a valid number."); // print error
    }
}