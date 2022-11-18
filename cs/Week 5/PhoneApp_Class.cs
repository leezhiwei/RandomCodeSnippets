
namespace PhoneApp_S10239812 // namespace to be used in Program.cs
{
    internal class Phone // phone class
    {
        private string phoneNum;
        private int usage; // private attributes
        private string planType;

        public string PhoneNum { get; set; }
        public int Usage { get; set; } // public properties
        public string PlanType { get; set; }

        public Phone()
        {
            PhoneNum = "0";
            Usage = 0; // default constructor with default values
            PlanType = "";
        }
        public Phone(string pn, int us, string ptype) // constructor that actually set the values of obj.
        {
            PhoneNum = pn;
            Usage = us; // pass it in to Properties
            PlanType = ptype;
        }
        public double CalculateCharge() // calculate charge mthod
        {
            if (PlanType == "A") // if A
            {
                double rate = 0.01 * 0.5; // 1 cent * half
                return rate * Usage; // return charged
            }
            else if (PlanType == "B") // else if B
            {
                if (Usage > 1000) // if more than 10000
                {
                    int charged = Usage - 1000; // then get value - 1000, since 1000 free
                    double rate = 0.01 * 0.2; // 1 cent * 0.2
                    return charged * rate; // return the charged amt
                }
                else // else less than 1000
                {
                    return 0; // return free
                }
            }
            else if (PlanType == "C") // else if plan is C
            {
                if (Usage > 5000) // more than 5000
                {
                    int charged = Usage - 5000; // get charged amt
                    double rate = 0.01 * 0.1; // rate is 1 cent * 0.1
                    return charged * rate; // return charged
                }
                else // else less than 5000
                {
                    return 0; // return free
                }
            }
            else // else not in A B C
            {
                return 0; // can't return null, so return 0
            }
        }
        public override string ToString() // override ToString method
        {
            return $"{PhoneNum}, {Usage}, {PlanType}"; // return 3 basic Properties seperated by comma
        }
    }
}
