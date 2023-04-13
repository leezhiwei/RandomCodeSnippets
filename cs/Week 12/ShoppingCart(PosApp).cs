using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PosApp
{
    internal class ShoppingCart
    {
        public List<CartItem> ItemList { get; set; } = new List<CartItem>();
        public ShoppingCart() { }
        public void AddItem(CartItem c)
        {
            ItemList.Add(c);
        }
        public List<CartItem> GetItemList()
        {
            return ItemList;
        }
        public bool RemoveItem(string c)
        {
            foreach (CartItem i in ItemList)
            {
                if (i.Code == c)
                {
                    ItemList.Remove(i);
                    return true;
                }
            }
            return false;
        }
        public void ClearCart()
        {
            ItemList = new List<CartItem>();
        }
        public int Size()
        {
            return ItemList.Count();
        }
        public bool IsEmpty()
        {
            if (ItemList.Count() == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
