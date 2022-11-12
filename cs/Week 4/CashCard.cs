namespace CashCardProject
{
    internal class CashCard
    {
        private string id; // init the private values
        private double balance;
        public string Id { get; set; } // ID property
        public double Balance { get; set; } // Balance property

        public CashCard() // default constructor default values
        {
            Id = "0";
            Balance = 0; // set 0
        }
        public CashCard(string id_1, double balance_1) // if specify values
        {
            Id = id_1; // let the values be the one entered
            Balance = balance_1;
        }

        public void TopUp(double amount) // for top up
        {
            Balance += amount; // just add to the property
        }
        public bool Deduct(double amount) // for deduct
        {
            double afterdeduct = Balance - amount; // get the deducted amount
            if (afterdeduct < 0) // if less than 0, or its -ve
            {
                return false; // return false and discard value
            }
            else // else +ve value
            {
                Balance = afterdeduct; // put the value into the balance
                return true; // return true bool
            }
        }
        public override string ToString() // get the string
        {
            return $"ID : {Id}\nBalance: ${Balance}"; // using format strings return ID and balance
        }
    }
}
