using System;

public class SavingsAccount
{
    public SavingsAccount(string no, string name, double bal)
    {
        AccountNo = no;
        AccountName = name;
        Balance = bal;
    }
    public void Deposit(double amount)
    {
        Balance = Balance + amount;
    }
    public bool Withdraw(double amount)
    {
        if (amount <= Balance)
        {
            Balance = Balance - amount;
            return true;
        }
        else
            return false;
    }
}

