double CalcDist(List<List<String>> mainlist, int firststop, int finalstop) // calculate distance fn
{
    double begdist = 0; // init both vars with 0
    double enddist = 0;
    int count = 0;
    foreach (var line in mainlist) // each line in the nested list
    {
        if (count == 0) // count == 0 ie header
        {
            count++;
            continue; // skip line by continue
        }
        if (Convert.ToInt32(line[1]) == firststop) // if first stop is in line
        {
            begdist = Convert.ToDouble(line[0]); // get the "distance" and put in var
        }
        else if (Convert.ToInt32(line[1]) == finalstop) // if last stop is in line
        {
            enddist = Convert.ToDouble(line[0]); // get "distance", put in var
        }
    }
   return enddist - begdist; // return final distance count
}
double DistFare(List<List<String>> dlist,double dist) // fare calc
{
    double value = 0;
    int count = 0; // init vars
    foreach (var line in dlist) // for each line in csv
    {
        if (count == 0)
        {
            count++; // skip first line (Description)
            continue;
        }
        if (dist <= Convert.ToDouble(line[0])) // if given dist is less than or equal to any value
        {
            value = Convert.ToDouble(line[1]) / 100; // get cents value
            break; // break loop
        }
    }
    return value; // then return value
}
String[] data = File.ReadAllLines("distance-based-fare.csv"); // read each line and put into a String[]
List<List<String>> dbfare = new List<List<String>>(); // init final nested list for distance fares
for (int x = 0; x < data.Length; x++) // for every line in the String[]
{
    List<String> list = new List<String>(data[x].Split(',')); // put new line into temp list, where each value is splitted by comma
    dbfare.Add(list); // add temp list to nested list
}
String[] busrawdata = File.ReadAllLines("bus_174.csv"); // read each line of 174 stops and put into String[]
List<List<String>> busstops = new List<List<String>>(); // init final nested list for distance fares
for (int x = 0; x < busrawdata.Length; x++) // for each line in the String[]
{
    List<String> list = new List<String>(busrawdata[x].Split(',')); // put new line into temp list, where each value is splitted by comma
    busstops.Add(list); // add temp list to nested list
}
foreach (var i in busstops) // for each line in busstops nested list
{
    Console.WriteLine($"{i[0].PadRight(20)}{i[1].PadRight(20)}{i[2].PadRight(20)}{i[3].PadRight(20)}");
    // Using formatting, print all elements with Padding on the right of 20 spaces
}
int boardingstop;
int alightingstop; // init the user input vars
while (true) // input loop
{
    Console.Write("Enter boarding bus stop: "); // prompt user for boarding stop
    string uinput1 = Console.ReadLine(); // get user input, store as string
    try
    {
        boardingstop = Convert.ToInt32(uinput1); // try to convert
    }
    catch
    {
        Console.WriteLine("Invalid input. Please put in a number"); // if cannot print error
        continue; // continue loop
    }
    Console.Write("Enter alighting bus stop: "); // prompt user for alighting stop
    string uinput2 = Console.ReadLine(); // get user input, store as string
    try
    {
        alightingstop = Convert.ToInt32(uinput2); // try convert
    }
    catch
    {
        Console.WriteLine("Invalid input. Please put in a number"); // if cannot print error
        continue; // continue loop
    }
    double distance = CalcDist(busstops, boardingstop, alightingstop); // use function to return distance
    if (distance <= 0) // if invalid distance (eg -ve values or 0)
    {
        Console.WriteLine("Invalid input of bus stop number, please try again."); // print error
        continue; // continue loop
    }
    Console.WriteLine($"The distance is {distance}km"); // print distance if valid
    double fare = DistFare(dbfare, distance); // use fn to get fare
    Console.WriteLine($"The fare is ${fare}"); // print out fare
    Console.WriteLine($"The estimated time is {distance * 4:F0} minutes"); // print estimated time with whole number ie no floating pt 
    break; // break outer loop once completed
}