using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PosApp
{
    internal class Product
    {
        public string Code { get; set; }
        public string Name { get; set; }
        public double Price { get; set; }
        public Product() { }
        public Product(string c, string n, double p)
        {
            Code = c;
            Name = n;
            Price = p;
        }
        public override string ToString()
        {
            return $"Code: {Code}, Name: {Name}, Price ${Price:F2}";
        }
    }
}
