// Not gonna comment each line, but basically write header, make new time object, and make new student object.
Console.WriteLine($"{"ID".PadRight(10)}{"Name".PadRight(10)}{"Tel".PadRight(10)}{"Date Of Birth".PadRight(10)}");
DateTime dob1 = new DateTime(2005, 09, 09);
Student s1 = new Student(1, "69999999", dob1, "Jane");
Console.WriteLine($"{Convert.ToString(s1.Id).PadRight(10)}{s1.Name.PadRight(10)}{s1.Tel.PadRight(10)}{s1.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
DateTime dob2 = new DateTime(2999, 12, 31);
Student s2 = new Student(2, "54321321", dob2, "John");
Console.WriteLine($"{Convert.ToString(s2.Id).PadRight(10)}{s2.Name.PadRight(10)}{s2.Tel.PadRight(10)}{s2.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
DateTime dob3 = new DateTime(3000, 12, 12);
Student s3 = new Student(3, "10000000", dob3, "Doe");
Console.WriteLine($"{Convert.ToString(s3.Id).PadRight(10)}{s3.Name.PadRight(10)}{s3.Tel.PadRight(10)}{s3.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
DateTime dob4 = new DateTime(1954, 12, 23);
Student s4 = new Student(4, "12345678", dob4, "Janay");
Console.WriteLine($"{Convert.ToString(s4.Id).PadRight(10)}{s4.Name.PadRight(10)}{s4.Tel.PadRight(10)}{s4.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
DateTime dob5 = new DateTime(1000, 4, 21);
Student s5 = new Student(5, "11111111", dob5, "Lasja");
Console.WriteLine($"{Convert.ToString(s5.Id).PadRight(10)}{s5.Name.PadRight(10)}{s5.Tel.PadRight(10)}{s5.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
List<Student> StudentList = new List<Student> { s1, s2, s3, s4, s5 }; // append objects to new list
void DisplayOutput(List<Student> sList) // DisplayOutput fn
{
    Console.WriteLine($"{"ID".PadRight(10)}{"Name".PadRight(10)}{"Tel".PadRight(10)}{"Date Of Birth".PadRight(10)}");
    // Header
    foreach (var s in sList) // for each object in list
    {
        Console.WriteLine($"{Convert.ToString(s.Id).PadRight(10)}{s.Name.PadRight(10)}{s.Tel.PadRight(10)}{s.DateOfBirth.Date.ToString("dd/MM/yyyy").PadRight(10)}");
        // print details
    }
}
DisplayOutput(StudentList); // run fn
Student GetStudent() // make getstudent fn, return Student object
{
    while (true) // input loop
    {
        Console.Write("What is your ID? "); // prompt id
        string idstr = Console.ReadLine(); // read id
        int id; // init id var
        try
        {
            id = Convert.ToInt32(idstr); // try to convert into int
        }
        catch
        {
            Console.WriteLine("Please enter a valid ID."); // if cannot error
            continue; // continue loop
        }
        Console.Write("What is your name? "); // prompt name
        string namestr = ""; // init string var
        namestr = Console.ReadLine(); // read input into var
        if (namestr == "") // if empty
        {
            Console.WriteLine("Please enter a valid name."); // prompt user
            continue; // continue loop
        }
        Console.Write("What is your phone number? "); // prompt for phone number
        string pnstr = Console.ReadLine(); // read input into var
        int pn; // init variable
        try
        {
            pn = Convert.ToInt32(pnstr); // try convert input into int
        }
        catch
        {
            Console.WriteLine("Please enter a valid phone number."); // if not error
            continue; // continue loop
        }
        Console.Write("What is your date of birth (In dd/MM/yyyy)? "); // prompt for DOB
        string dobstr = Console.ReadLine(); // put user input into string 
        DateTime dob; // init datetime variable
        try
        {
            dob = Convert.ToDateTime(dobstr);  // try to convert
        }
        catch
        {
            Console.WriteLine("Please enter a date."); // if not print error
            continue; // restart loop
        }
        return new Student(id, Convert.ToString(pn), dob, namestr); // return Student object
        break; // break loop
    }
    }
StudentList.Add(GetStudent()); // run fn and add object to list
DisplayOutput(StudentList); // display updated list
String[] csvdata = File.ReadAllLines("Students.csv"); // read csv to stringlist
List<List<String>> csvlist = new List<List<String>>(); // make new string list from reading csv 
for (int x = 1; x < csvdata.Length; x++) // convert string list to splitted by comma
{
    List<String> list = new List<String>(csvdata[x].Split(',')); // temp list with splitted value
    csvlist.Add(list); // add to nested list the temp list
}
List<Student> StudentList2 = new List<Student>(); // object list for Student
foreach (var line in csvlist) // for each line in the nested list
{
    Student student = new Student(Convert.ToInt32(line[0]), line[2], Convert.ToDateTime(line[3]), line[1]);
    // create temp student object
    StudentList2.Add(student); // add the temp object to list
}
DisplayOutput(StudentList2); // show the new object list