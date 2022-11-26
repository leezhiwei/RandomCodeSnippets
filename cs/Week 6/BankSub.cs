namespace Bank_SubClass
{
    internal class SavingsAccount:BankAccount
    {
        private double rate;
        public double Rate { get; set; }
        public SavingsAccount():base()
        {
            Rate = 0;
        }
        public SavingsAccount(string ano, string acn, double bal, double ra):base(ano,acn,bal)
        {

            Rate = ra;
        }
        public double CalculateInterest()
        {
            return Balance * Rate / 100;
        }
        public override string ToString()
        {
            return base.ToString() + $" Interest Rate:{Rate}% Interest:${CalculateInterest()}";
        }
    }
}
