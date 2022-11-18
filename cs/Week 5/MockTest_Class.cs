namespace MockTest
{
    internal class Inventory
    {
        private int itemID;
        private string prodName;
        private double unitPrice; // create attributes (private vars)
        private string itemDesc;
        private int amountofInv;

        public int ItemID { get; set; }
        public string ProdName { get; set; }
        public double UnitPrice { get; set; } // create the properties (accessible by public)
        public string ItemDesc { get; set; }
        public int AmountofInv { get; set; }

        public Inventory(int id, string name, double price, string desc, int qty) // constructor with values
        {
            ItemID = id;
            ProdName = name;
            UnitPrice = price; // assign them to the property
            ItemDesc = desc;
            AmountofInv = qty;
        }
        public double CalculateTotalValue() // method to calculate total value of inventory
        {
            return UnitPrice * AmountofInv; // return total amount of goods
        }
        public double CalculateTotalAddGST() // method to calculate total value adding GST
        {
            return CalculateTotalValue() * 1.07; // call previous function and multiply by 107%
        }
        public override string ToString() // Tostring fn
        {
            return ItemID + ' ' + ProdName + ' ' + UnitPrice + ' ' + ItemDesc + ' ' + AmountofInv; // return all value as string
        }
    }
}
