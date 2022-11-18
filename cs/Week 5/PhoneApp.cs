using PhoneApp_S10239812; // using the class namespace

List<Phone> phonelist = new List<Phone>(); // create a List of Phone objects
void InitialiseList(List<Phone> plist) // init method, pass through the list, no need return anything
{
    String[] data = File.ReadAllLines("PhoneDetails.csv"); // create stringlist from csv
    for (int x = 1; x < data.Length; x++) // process every line, except for line 1 (header)
    {
        String[] splitted = data[x].Split(","); // split each line by comma
        phonelist.Add(new Phone(splitted[0], Convert.ToInt32(splitted[1]), splitted[2]));
        // create new object and add to Phone object list
    }
}
InitialiseList(phonelist); // call the method
void DisplayOutput(List<Phone> plist) // method for display
{
    Console.WriteLine($"{"PhoneNo".PadRight(15)} {"Usage".PadRight(15)} {"PlanType".PadRight(15)} {"PhoneCharge($)".PadRight(15)}");
    // for header, padright will pad string to the inputted amount, eg 15
    foreach (Phone phone in plist) // for each phone object in plist
    {
        string pcharge = $"{phone.CalculateCharge():F2}"; // make the charge 2 floating point first
        Console.WriteLine($"{phone.PhoneNum.PadRight(15)} {phone.Usage.ToString().PadRight(15)} {phone.PlanType.PadRight(15)} {pcharge.PadRight(15)}");
        // each properties are converted with ToString() if not already string, and will be padded same.
    }
}
DisplayOutput(phonelist); // call the method
Phone findnum(List<Phone> plist, string phonenum) // find the phone number method
{
    foreach(Phone phone in plist) // for each phone object in the list
    {
        if (phone.PhoneNum == phonenum) // if phone object number is same as input
        {
            return phone; // return the object
        }
    }
    return null; // else return null
}
bool UpdateUsage(List<Phone> plist, string phoneno, int usage) // update usage method with return bool
{
    foreach(Phone phone in plist) // for each phone object in the list
    {
        if (phone.PhoneNum == phoneno) // if number matches
        {
            phone.Usage = usage; // reinit property with new values
            return true; // return true bool
        }
    }
    return false; // if not return false bool
}
string text = "Update Phone Usage"; // header to display
string dashes = new string('-', text.Length); // create same amount of dashes
Console.WriteLine(text); // write header to console
Console.WriteLine(dashes); // also write dashes to console
Console.Write("Enter Phone no: "); // prompt user for the number
string pn = Console.ReadLine(); // get the number and store into pn
Phone phoneobj = findnum(phonelist, pn); // get object from function
if (phoneobj is not null) // if not null
{
    Console.WriteLine($"Current usage: {phoneobj.Usage}"); // display current usage
    Console.Write("Enter new usage: "); // prompt for new usage
    int newusage = Convert.ToInt32(Console.ReadLine()); 
    // convert directly to int, no input validation, so will crash if value wrong
    if (UpdateUsage(phonelist, pn, newusage)) // if method returns true
    {
        Console.WriteLine("The new usage is updated successfully"); // print success message
        DisplayOutput(phonelist); // print out new list
    }
    else // if not successful
    {
        Console.WriteLine("Unsuccessful update."); // return an unsuccessful message
    }
}
else // if object is null
{
    Console.WriteLine("Phone not found!"); // show error
}