using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CashCardDemoApp
{
    internal class MemberCashCard: CashCard
    {
        // Property
        public int Points { get; set; }

        // Constructors
        public MemberCashCard() : base() { }
        public MemberCashCard(string id, double b) : base(id, b)
        {
        }

        public void AddPoints(int pt)
        {
            Points += pt;
        }

        public bool DeductPoints(int pt)
        {
            if (Points >= pt)
            {
                Points -= pt;
                return true;
            }
            else
                return false;
        }
        public override bool Deduct(double amt)
        {
            if (base.Deduct(amt))
            {
                AddPoints(Convert.ToInt32(amt / 5));
                return true;
            }
            else
                return false;

        }

        public override string ToString()
        {
            return base.ToString() + " Points: " + Points;
        }
    }
}
