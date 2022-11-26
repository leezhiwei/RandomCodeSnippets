
using System;
using System.Collections.Generic;
using CashCardDemoApp;

// create a cashcard
CashCard myCashCard = new CashCard("101", 10);
Console.WriteLine("My cashcard: {0}", myCashCard);

// top up $10 to the card
Console.WriteLine("\nAttempting top up for cash card...");
myCashCard.TopUp(10);
Console.WriteLine("My cashcard: {0}", myCashCard);

// deduct $11 from the card
Console.WriteLine("\nAttempting deduction from cash card...");
bool success = myCashCard.Deduct(11);
if (success)
    Console.WriteLine("$11 deducted successfully.");
else
    Console.WriteLine("Unable to deduct $11.");

Console.WriteLine("My cashcard: {0}", myCashCard);

// create member cashcard
MemberCashCard myMemberCashCard = new MemberCashCard("201", 10);
Console.WriteLine("\nMy member cashcard: {0}", myMemberCashCard);

// top up $10 to the card
Console.WriteLine("\nAttempting top up for member cash card...");
myMemberCashCard.TopUp(10);
Console.WriteLine("My member cashcard: {0}", myMemberCashCard);

// deduct $11 from the card
Console.WriteLine("\nAttempting deduction from member cash card...");
success = myMemberCashCard.Deduct(11);
if (success)
    Console.WriteLine("$11 deducted successfully.");
else
    Console.WriteLine("Unable to deduct $11.");

Console.WriteLine("My member cashcard: {0}", myMemberCashCard);