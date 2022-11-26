namespace Bank_SubClass
{
    internal class BankAccount
    {
        private string accNo;
        private string accName;
        private double balance;

        public string AccNo { get; set; }
        public string AccName { get; set; }
        public double Balance { get; set; }

        public BankAccount()
        {
            AccNo = "";
            AccName = "";
            Balance = 0;
        }
        public BankAccount(string ano, string acn, double bal)
        {
            AccNo = ano;
            AccName = acn;
            Balance = bal;
        }
        public void Deposit(double amt)
        {
            Balance += amt;
        }
        public bool Withdraw(double amt)
        {
            if ((Balance - amt) < 0)
            {
                return false;
            }
            else
            {
                Balance -= amt;
                return true;
            }
        }
        public override string ToString()
        {
            return $"Account Number: {AccNo} Account Name: {AccName} Balance: ${Balance}";
        }
    }
}
