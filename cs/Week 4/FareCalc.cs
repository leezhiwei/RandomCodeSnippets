using FareCalcClasses;
double CalcDist(List<BusStop> busstop, int firststop, int finalstop) // calculate distance fn
{
    double begdist = 0; // init both vars with 0
    double enddist = 0;
    foreach (BusStop line in busstop) // each line in the List of objects
    {
        if (Convert.ToInt32(line.ToString().Split(',')[1]) == firststop) // if first stop is in line
        {
            begdist = Convert.ToDouble(line.ToString().Split(',')[0]); // get the "distance" and put in var
        }
        else if (Convert.ToInt32(line.ToString().Split(',')[1]) == finalstop) // if last stop is in line
        {
            enddist = Convert.ToDouble(line.ToString().Split(',')[0]); // get "distance", put in var
        }
    }
    return enddist - begdist; // return final distance count
}
double DistFare(List<Fare> farelist, double dist) // fare calc
{
    double value = 0;
    foreach (Fare fare in farelist) // for each line in object list
    {
        if (dist <= Convert.ToDouble(fare.ToString().Split(',')[0])) // if given dist is less than or equal to any value
        {
            value = Convert.ToDouble(fare.ToString().Split(',')[1]) / 100; // get cents value
            break; // break loop
        }
    }
    return value; // then return value
}
List<BusStop> busStopList = new List<BusStop>(); // new busstop object
List<Fare> farelist = new List<Fare>(); // new farelist object
String[] data = File.ReadAllLines("bus_174.csv"); // read each line and put into a String[]
for (int x = 1; x < data.Length; x++) // for every line in the String[]
{
    String[] templist = data[x].Split(','); // split line to templist
    busStopList.Add(new BusStop(Convert.ToDouble(templist[0]), templist[1], templist[2], templist[3])); // add busstop object to list
}
String[] data1 = File.ReadAllLines("distance-based-fare.csv"); // read each line and put into a String[]
for (int x = 1; x < data1.Length; x++) // for every line in the String[]
{
    String[] templist1 = data1[x].Split(','); // split line to templist1
    farelist.Add(new Fare(Convert.ToDouble(templist1[0]), Convert.ToInt32(templist1[1]))); // add fare object to list
}
Console.WriteLine($"{"Distance (km)".PadRight(20)}{"Bus Stop Code".PadRight(20)}{"Road".PadRight(20)}{"Bus Stop Description".PadRight(20)}"); // print header
foreach (BusStop busstop in busStopList) // for each line in busstops nested list
{
    List<string> temp = new List<string>(busstop.ToString().Split(',')); // split object to individual component
    Console.WriteLine($"{temp[0].PadRight(20)}{temp[1].PadRight(20)}{temp[2].PadRight(20)}{temp[3].PadRight(20)}"); // print out
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
    double distance = CalcDist(busStopList, boardingstop, alightingstop); // use function to return distance
    if (distance <= 0) // if invalid distance (eg -ve values or 0)
    {
        Console.WriteLine("Invalid input of bus stop number, please try again."); // print error
        continue; // continue loop
    }
    Console.WriteLine($"The distance is {distance}km"); // print distance if valid
    double fare = DistFare(farelist, distance); // use fn to get fare
    Console.WriteLine($"The fare is ${fare}"); // print out fare
    Console.WriteLine($"The estimated time is {distance * 4:F0} minutes"); // print estimated time with whole number ie no floating pt 
    break; // break outer loop once completed
}