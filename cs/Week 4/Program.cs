SavingsAccount acc1 = new SavingsAccount("111", "Joe", 200.0);
SavingsAccount acc2 = new SavingsAccount("112", "Mary", 2000.0);

acc1.Withdraw(50);
Console.WriteLine($"Balance of Acc 1:{acc1.Balance}");
