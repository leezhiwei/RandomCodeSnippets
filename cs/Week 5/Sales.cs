using Sales;
List<Item> itemlist = new List<Item>();
void initlist()
{
    String[] data = File.ReadAllLines("sales.csv");
    for (int x = 1; x < data.Length; x++)
    {
        String[] line = data[x].Split(",");
        itemlist.Add(new Item(line[0], line[1], Convert.ToInt32(line[2]), Convert.ToDouble(line[3])));
    }
}
initlist();
void display(List<Item> itemlist)
{
    Console.WriteLine($"{"Code".PadRight(6)} {"Name".PadRight(15)} {"Quantity".PadRight(15)} {"Price($)".PadLeft(15)} {"Amount($)".PadLeft(15)} {"GST($)".PadLeft(15)} {"Total($)".PadLeft(15)}");
    foreach (Item item in itemlist)
    {
        string price = $"{item.Price:F2}";
        string amount = $"{item.CalculateTotalPrice():F2}";
        string gst = $"{item.CalculateGST():F2}";
        string total = $"{item.CalculateTotal():F2}";
        Console.WriteLine($"{item.Code.PadRight(6)} {item.Name.PadRight(15)} {item.Qty.ToString().PadRight(15)} {price.PadLeft(15)} {amount.PadLeft(15)} {gst.PadLeft(15)} {total.PadLeft(15)}");
    }
}
display(itemlist);
List<Item> higherthansales(List<Item> ilist, double target)
{
    List<Item> returnlist = new List<Item>();
    foreach (Item item in ilist)
    {
        if (item.CalculateTotal() > target)
        {
            returnlist.Add(item);
        }
    }
    if (returnlist.Count <= 0)
    {
        return null;
    }
    else
    {
        return returnlist;
    }
    
}
string text = "Display Sales Above Target";
string dash = new string('-', text.Length + 1);
Console.WriteLine(text);
Console.WriteLine(dash);
Console.Write("Enter the target amount($): ");
double amount = Convert.ToDouble(Console.ReadLine());
List<Item> list1 = higherthansales(itemlist, amount);
if (list1 == null)
{
    Console.WriteLine("No sales above the target.");
}
else
{
    display(list1);
}