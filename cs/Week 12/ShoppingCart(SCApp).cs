using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShoppingCartApp
{
    internal class ShoppingCart
    {
        public string CartId { get; set; }
        public List<CartItem> ItemList { get; set; }
                             = new List<CartItem>();
	public ShoppingCart() { }

    public ShoppingCart(string id)
    {
        CartId = id;
    }

    public void AddItem(CartItem item)
    {
         ItemList.Add(item);
    }
    }
}
