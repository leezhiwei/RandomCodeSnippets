using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CashCardDemoApp
{
    internal class CashCard
    {
        // Properties 
        public string Id { get; set; }
        public double Balance { get; set; }

        // Constructors
        public CashCard() { }
        public CashCard(string i, double b)
        {
            Id = i;
            Balance = b;
        }

        // Other methods
        public void TopUp(double amt)
        {
            Balance += amt;
        }
        public virtual bool Deduct(double amt)
        {
            if (Balance >= amt)
            {
                Balance -= amt;
                return true;
            }
            else
                return false;
        }
        public override string ToString()
        {
            return "Id:" + Id + " Balance:" + Balance;
        }
    }
}
