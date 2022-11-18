namespace Sales
{
    internal class Item
    {
        private string code;
        private string name;
        private int qty;
        private double price;

        public string Code { get; set; }
        public string Name { get; set; }
        public int Qty { get; set; }
        public double Price { get; set; }

        public Item()
        {
            Code = "";
            Name = "";
            Qty = 0;
            Price = 0;
        }
        public Item(string c, string n, int q, double p)
        {
            Code = c;
            Name = n;
            Qty = q;
            Price = p;
        }
        public double CalculateTotalPrice()
        {
            return Qty * Price;
        }
        public double CalculateGST()
        {
            return CalculateTotalPrice() * 0.07;
        }
        public double CalculateTotal()
        {
            return CalculateTotalPrice() + CalculateGST();
        }
        public override string ToString()
        {
            return $"{Code}, {Name}, {Qty}, {Price}";
        }
    }
}
