namespace EmployeeApp
{
    internal class PartTimeEmployee:Employee
    {
        private double dailyRate;
        private int daysWorked;
        public double DailyRate { get; set; }
        public int DaysWorked { get; set; }
        public PartTimeEmployee() : base()
        {
            DailyRate= 0;
            DaysWorked= 0;
        }
        public PartTimeEmployee(int i, string n, double dr, int dw):base(i,n)
        {
            DailyRate= dr;
            DaysWorked= dw;
        }
        public override double CalculatePay()
        {
            return DaysWorked * DailyRate;
        }
        public override string ToString()
        {
            return base.ToString() + $"Daily Rate: ${DailyRate:F2} Days Worked: {DaysWorked} days";
        }
    }
}
