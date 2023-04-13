using PosApp;
List<Product> productList = new List<Product>();
productList.Add(new Product("1001", "Apple iPhone", 1088));
productList.Add(new Product("1005", "HTC Sensation", 888));
productList.Add(new Product("1013", "LG Optimus 2X", 788));
productList.Add(new Product("1022", "Motorola Atrix", 958));
productList.Add(new Product("1027", "Samsung Galaxy", 988));
ShoppingCart sc = new ShoppingCart();
void DisplayMenu()
{
    Console.WriteLine("---------------- M E N U -----------------");
    Console.WriteLine("[1] List all products and prices");
    Console.WriteLine("[2] Add item to cart");
    Console.WriteLine("[3] View cart items");
    Console.WriteLine("[4] Remove item from cart");
    Console.WriteLine("[5] Clear cart items");
    Console.WriteLine("[0] Exit");
    Console.WriteLine("------------------------------------------");
}
void DisplayProd()
{
    foreach (Product p in productList)
    {
        Console.WriteLine(p.ToString());
    }
}
while (true)
{
    DisplayMenu();
    Console.Write("Enter your option: ");
    string s = Console.ReadLine();
    if (s == "0")
    {
        break;
    }
    else if (s == "1")
    {
        DisplayProd(); 
    }
    else if (s == "2")
    {
        DisplayProd();
        bool found = false;
        while (true)
        {
            Console.Write("Which product number do you want to add: ");
            string read = Console.ReadLine();
            foreach (Product p in productList)
            {
                if (p.Code == read)
                {
                    Console.Write("Quantity of product: ");
                    int q = 0;
                    try
                    {
                        q = Convert.ToInt32(Console.ReadLine());
                    }
                    catch
                    {
                        Console.WriteLine("Please enter a number");
                        continue;
                    }
                    sc.AddItem(new CartItem(p.Code, p.Name, p.Price, q));
                    found = true;
                    break;
                }
            }
            break;
        }
        if (!found)
        {
            Console.WriteLine("Item not found.");
        }
    }
    else if (s == "3")
    {
        string finalstr = "";
        double total = 0;
        foreach (CartItem c in sc.GetItemList())
        {
            finalstr += c.ToString() + "\n";
            total += c.Price * c.Qty;
        }
        Console.WriteLine(finalstr);
        Console.WriteLine($"Total price: ${total:F2}");
    }
    else if (s == "4")
    {
        foreach (CartItem c in sc.GetItemList() )
        {
            Console.WriteLine(c.ToString());
        }
        Console.Write("Which item number do you want to remove: ");
        string itemcode = Console.ReadLine();
        if (!sc.RemoveItem(itemcode))
        {
            Console.WriteLine("Invalid item code");
        }
        else
        {
            Console.WriteLine("Successful removal.");
        }
    }
    else if (s == "5")
    {
        sc.ClearCart();
    }
    else
    {
        Console.WriteLine("Invalid option");
    }
}