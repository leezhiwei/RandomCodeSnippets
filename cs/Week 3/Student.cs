class Student
{
    //Question 1
    //Complete the missing attributes & Properties and the incomplete student class constructor

    // attributes and properties
    private int id;
    private string name;
    private string tel;

    public string Tel
    {
        get { return tel; }
        set { tel = value; }
    }
    public int Id
    {
        get { return id; }
        set { id = value; }
    }
    public string Name
    {
        get { return name; }
        set { name = value; }
    }
    private DateTime dateOfBirth;

    public DateTime DateOfBirth
    {
        get { return dateOfBirth; }
        set { dateOfBirth = value; }
    }

    // constructor
    public Student(int i, string t, DateTime dob, string n)
    {
        Tel = t;
        DateOfBirth = dob;
        Id = i;
        Name = n;
    }
}