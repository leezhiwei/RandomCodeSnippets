using MockTest; // use the defined class
List<Inventory> invlist = new List<Inventory>(); // create new object list
void initlist(List<Inventory> list) // initialise list
{
    String[] data = File.ReadAllLines("Inventory.dsv"); // read all lines into string list
    for (int x = 1; x < data.Length; x++) // for each line in the list, except header
    {
        String[] linesplitted = data[x].Split('.'); // split by dot
        invlist.Add(new Inventory(Convert.ToInt32(linesplitted[0]), linesplitted[1], Convert.ToDouble(linesplitted[2]), linesplitted[3], Convert.ToInt32(linesplitted[4])));
        // add to object
    }
}
initlist(invlist); // run fn
void display(List<Inventory> ilist) // display function
{
    Console.WriteLine($"{"ID".PadRight(15)} {"Name".PadRight(30)} {"Unit Price ($)".PadRight(15)} {"Description".PadRight(15)} {"Stock Amount".PadRight(15)} {"Total Price ($)".PadRight(15)}");
    // write header
    foreach (Inventory inv in invlist) // for each object in list
    {
        string finalstring = ""; // create empty string for substring to be in
        if (inv.ItemDesc.Length > 15) // if description is more than 15
        {
            finalstring = inv.ItemDesc.Substring(0, 15); // shorten using substring function
        }
        else // if shorter than 15
        {
            finalstring = inv.ItemDesc; // finalstring is equals to original string
        }
        string unitprice = $"{inv.UnitPrice:F2}"; // make a string to 2dp for unitprice
        string totalprice = $"{inv.CalculateTotalAddGST():F2}"; // make a string to 2dp for unitprice
        Console.WriteLine($"{inv.ItemID.ToString().PadRight(15)} {inv.ProdName.PadRight(30)} {unitprice.PadRight(15)} {finalstring.PadRight(15)} {inv.AmountofInv.ToString().PadRight(15)} {totalprice.PadRight(15)}");
        // write each object to console
    }
}
display(invlist); // run the fn
bool inlist(List<Inventory> ilist, int input) // inlist fn
{
    foreach(Inventory inv in ilist) // for each object in list
    {
        if (input == inv.ItemID) // if id matched
        {
            return true; // return true
        }
    }
    return false; // if not, return false
}
Console.Write("Please enter the new ID that you want to add: "); // get user input for ID
int id = Convert.ToInt32(Console.ReadLine()); // put into variable
if (inlist(invlist, id)) // if true
{
    Console.WriteLine("Item already in list");// print output and skip else
}
else // if not inside
{
    Console.Write("What is the name of item: "); // prompt for name
    string name = Console.ReadLine(); // get name
    Console.Write("What is the price per unit of item: "); // prompt for price
    double unitprice = Convert.ToDouble(Console.ReadLine()); // get price
    Console.Write("What is the number of items: "); // prompt for quantity
    int amt = Convert.ToInt32(Console.ReadLine()); // get quantity
    Console.Write("What is the description of item: "); // prompt for description
    string desc = Console.ReadLine(); // get description
    invlist.Add(new Inventory(id, name, unitprice, desc, amt)); // add object to list
    display(invlist); // display list
}
double total = 0; // init total value
foreach(Inventory inv in invlist) // for each object in the list
{
    total += inv.CalculateTotalAddGST(); // add the total to the variable
}
Console.WriteLine($"The total amount of assets with GST is ${total:F2}"); 
// print it out with only 2 floating point
foreach(Inventory inv in invlist) // for each object in list
{
    if (inv.ItemID == 53) // if ItemID is 53
    {
        inv.UnitPrice = inv.UnitPrice * 0.95; // multiply by 95%
        inv.AmountofInv = 287; // and reduce quantity
    }
}
display(invlist); // display the list