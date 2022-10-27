while (true)
{
    Console.Write("Enter amount in dollars: "); // user input prompt
    string price = Console.ReadLine(); // convert user input to double
    double pricedouble;
    try
    {
        pricedouble = Convert.ToDouble(price);
    }
    catch
    {
        Console.WriteLine("Please input a number.");
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