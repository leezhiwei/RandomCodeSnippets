int phoneno; // init variable
while (true) // input loop
{
    Console.Write("What is the name that you want to append? "); // prompt for name
    string name = Console.ReadLine(); // get name and store in var
    if (name == "Exit") // if exit by user
    {
        break; // break the loop
    }
    else if (name == "") // if blank name
    {
        Console.WriteLine("Please enter a valid name"); // error to user
        continue; // continue loop
    }
    Console.Write($"What is {name}'s phone number? "); // ask for phone number
    string inputphone = Console.ReadLine(); // store the input in var
    try
    {
        phoneno = Convert.ToInt32(inputphone); // try to convert to int
    }
    catch
    {
        Console.WriteLine("Invalid phone number"); // if cannot error user
        continue; // continue loop 
    }
    using (StreamWriter file = new StreamWriter("phoneno.csv", true)) // open file as append
    {
        file.WriteLine($"\n{name}, {phoneno}"); // write the data
    }
}