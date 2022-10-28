String[] data = File.ReadAllLines("loaninfo.csv"); // read csv file into String[] with lines
List<List<string>> maxlines = new List<List<String>> (); // init nested final list
for (int x = 0; x < data.Length; x++) // for each line of the String[]
{
    List<string> datalines = new List<String>(data[x].Split(',')); // temp list with line of String[] where values are splitted by comma
    maxlines.Add(datalines); // add temp list to the final nested list
}
int count = 0; // init variable count
List<List<string>> overdueinfo = new List<List<String>>(); // init overdue info nested list
foreach (var line in maxlines) // for each value in nested list
{
    if (count == 0) // if first line only print
    {
        Console.WriteLine($"{line[0].PadRight(15)}{line[1].PadRight(15)}{line[2].PadRight(15)}{line[3].PadRight(15)}{"Days Loan".PadRight(15)}{"Days Overdue".PadRight(15)}{"Fine".PadRight(15)}");
        // print the description
        count++; // increment count
        continue; // continue loop (no processing needed)
    }
    var begindate = DateTime.Parse(line[2]); // get initial out date
    var enddate = DateTime.Parse(line[3]); // get the ending in date
    int dur = (enddate - begindate).Days; // get duration amount and convert it from duration to int, days
    int overdueby = 0; // init overdueby var
    double fine = 0; // init fine var
    if (dur > 14) // if duration over 14, eg overdue
    {
        overdueby = dur - 14; // get overdue by how long
        fine = overdueby * 0.5; // get the fine value in $
        List<String> person = new List<string>{ line[0], line[1], Convert.ToString(overdueby), Convert.ToString(fine) };
        // add to temp list
        overdueinfo.Add(person); // add to final overdue persons list
    }
    Console.WriteLine($"{line[0].PadRight(15)}{line[1].PadRight(15)}{line[2].PadRight(15)}{line[3].PadRight(15)}{Convert.ToString(dur).PadRight(15)}{Convert.ToString(overdueby).PadRight(15)}${fine:F2}");
    // print out all of the values to console
    count++; // increment count
}
using (StreamWriter output = new StreamWriter("overdueinfo.csv")) // create this overdueinfo or override
{
    output.WriteLine("Book ID, Borrower ID, Days Overdue, Fine Amount"); // write the first line, heading
    foreach (var line in overdueinfo) // for each line in nested list
    {
        output.WriteLine($"{line[0]},{line[1]},{line[2]},{line[3]}"); // write the lines
    }
    Console.WriteLine($"Written {overdueinfo.Count} lines into overdueinfo.csv"); // output to console how many lines
}
