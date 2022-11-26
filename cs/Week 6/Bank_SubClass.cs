using Bank_SubClass;
using System.Reflection.Metadata.Ecma335;

List<SavingsAccount> acclist = new List<SavingsAccount>();
void InitList(List<SavingsAccount> list)
{
    String[] data = File.ReadAllLines("savings_account.csv");
    for (int x = 1; x < data.Length; x++)
    {
        String[] splitted = data[x].Split(',');
        list.Add(new SavingsAccount(splitted[0], splitted[1], Convert.ToDouble(splitted[2]), Convert.ToDouble(splitted[3])));
    }
}
InitList(acclist);
void DisplayAll(List<SavingsAccount> sList)
{
    foreach (SavingsAccount s in sList)
    {
        Console.WriteLine(s.ToString());
    }
}
SavingsAccount Search(List<SavingsAccount> sList, string accNo)
{
    foreach (SavingsAccount s in sList)
    {
        if (accNo == s.AccNo)
        {
            return s;
        }
    }
    return null;
}
void DisplayMenu()
{
    Console.WriteLine("Menu");
    Console.WriteLine("[1] Display all accounts");
    Console.WriteLine("[2] Deposit");
    Console.WriteLine("[3] Withdraw");
    Console.WriteLine("[0] Exit");
}
while (true)
{
    DisplayMenu();
    Console.Write("Enter your option: ");
    int option = Convert.ToInt32(Console.ReadLine());
    if (option == 1)
    {
        DisplayAll(acclist);
    }
    else if (option == 2)
    {
        Console.Write("Enter your account number: ");
        string an = Console.ReadLine();
        SavingsAccount foundobj = Search(acclist, an);
        if (foundobj is null)
        {
            Console.WriteLine("There is no such account, please try again.");
            continue;
        }
        else
        {
            Console.Write("Amount to deposit: ");
            double amt = Convert.ToDouble(Console.ReadLine());
            foundobj.Deposit(amt);
            Console.WriteLine($"${amt} is deposited successfully");
            Console.WriteLine(foundobj.ToString());
        }
    }
    else if (option == 3)
    {
        Console.Write("Enter your account number: ");
        string an = Console.ReadLine();
        SavingsAccount foundobj = Search(acclist, an);
        if (foundobj is null)
        {
            Console.WriteLine("There is no such account, please try again.");
            continue;
        }
        else
        {
            Console.Write("Amount to withdraw: ");
            double amt = Convert.ToDouble(Console.ReadLine());
            bool result = foundobj.Withdraw(amt);
            if (result)
            {
                Console.WriteLine($"${amt} is withdrawn successfully");
            }
            else
            {
                Console.WriteLine("Insufficient funds.");
                continue;
            }
            Console.WriteLine(foundobj.ToString());
        }
    }
    else if (option == 0)
    {
        string text = "Goodbye!";
        string dash = new string('-', text.Length);
        Console.WriteLine(dash);
        Console.WriteLine(text);
        Console.WriteLine(dash);
        break;
    }
    else
    {
        Console.WriteLine("Invalid Option.");
        continue;
    }
}
