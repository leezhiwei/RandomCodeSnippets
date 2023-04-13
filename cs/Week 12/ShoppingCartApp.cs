using ShoppingCartApp;
ShoppingCart shop1 = new ShoppingCart("1");
shop1.AddItem(new CartItem(1, "Logitech Mouse", 40.0, 2));
shop1.AddItem(new CartItem(2, "Logitech Keyboard", 60.0, 1));
List<CartItem> cartlist = shop1.ItemList;
string finalstr = "";
double totalprice = 0;
foreach (CartItem item in cartlist)
{
    finalstr += item.ToString() + "\n";
    totalprice += item.Price * item.Qty;
}
Console.WriteLine(finalstr);
Console.WriteLine($"The total price of all the product in cart is ${totalprice:F2}");