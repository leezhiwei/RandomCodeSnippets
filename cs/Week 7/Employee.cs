namespace EmployeeApp
{
    abstract class Employee:IComparable<Employee>
    {
        private int id;
        private string name;
        public int Id { get; set; }
        public string Name { get; set; }

        public int CompareTo(Employee e)
        {
            return e.Id.CompareTo(id);
        }
        public Employee()
        {
            Id = 0;
            Name = "";
        }
        public Employee(int i, string n)
        {
            Id = i;
            Name = n;
        }
        public abstract double CalculatePay();
        public override string ToString()
        {
            return $"Name: {Name} ID: {Id} ";
        }
    }
}
