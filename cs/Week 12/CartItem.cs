using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShoppingCartApp
{
    internal class CartItem
    {
        public int Code { get; set; }
        public string Name { get; set; }
        public double Price { get; set; }
        public int Qty { get; set; }
        public CartItem() { }
        public CartItem(int c, string n, double p, int q)
        {
            Code = c;
            Name = n;
            Price = p;
            Qty = q;
        }
        public override string ToString()
        {
            return $"Code: {Code}, Name: {Name}, Price: ${Price:F2}, Quantity: {Qty} pieces";
        }
    }
}
