namespace EmployeeApp
{
    internal class FullTimeEmployee:Employee
    {
        private double basicPay;
        private double allowance;
        public double BasicPay { get; set; }
        public double Allowance { get; set; }
        public FullTimeEmployee(): base()
        {
            basicPay = 0;
            allowance = 0;
        }
        public FullTimeEmployee(int i, string n, double b, double a) : base(i, n)
        {
            BasicPay= b;
            Allowance= a;
        }
        public override double CalculatePay()
        {
            return BasicPay + Allowance;
        }
        public override string ToString()
        {
            return base.ToString() + $"Basic Pay: ${BasicPay:F2} Allowance: ${Allowance:F2}";
        }
    }
}
