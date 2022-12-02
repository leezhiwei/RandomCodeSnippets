using EmployeeApp;
List<Employee> elist = new List<Employee>();
Employee fte = new FullTimeEmployee(103,"John",1500,100);
elist.Add(fte);
Employee pte = new PartTimeEmployee(101, "Mary", 50, 10);
elist.Add(pte);
elist.Sort();
foreach (Employee e in elist)
{
    Console.WriteLine(e.ToString());
}