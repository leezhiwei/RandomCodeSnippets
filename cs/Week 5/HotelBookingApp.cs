using HotelBookingApp;
List<Booking> bookings = new List<Booking>();
void initlist(List<Booking> book)
{
    String[] data = File.ReadAllLines("bookings.csv"); // read each line and put into a String[]
    for (int x = 1; x < data.Length; x++)
    {
        String[] templist = data[x].Split(',');
        Booking booking = new Booking(Convert.ToInt32(templist[0]), templist[1], Convert.ToDateTime(templist[2]), Convert.ToDateTime(templist[3]), Convert.ToDouble(templist[4]));
        book.Add(booking);
    }
}
initlist(bookings);
void displaybook(List<Booking> book)
{
    Console.WriteLine($"{"Booking #".PadRight(15)} {"Name".PadRight(15)} {"Date In".PadRight(15)} {"Date Out".PadRight(15)} {"Rate($)".PadRight(15)} {"Days".PadRight(15)} {"Charge($)".PadRight(15)}");
    foreach (Booking booking in book)
    {
        string rate = $"{booking.Rate:F2}";
        Console.WriteLine($"{booking.BookingNo.ToString().PadRight(15)} {booking.Name.PadRight(15)} {booking.DateIn.ToString("dd/MM/yyyy").PadRight(15)} {booking.DateOut.ToString("dd/MM/yyyy").PadRight(15)} {rate.PadRight(15)} {booking.CalculateDuration(booking).ToString().PadRight(15)} {booking.CalculateCharge(booking, booking.Rate):F2}");
    }
}
displaybook(bookings);
bool updateroomrate(int bookno, double nrate, List<Booking> books, int args)
{
    if (args == 0)
    {
        foreach (Booking book in books)
        {
            if (bookno == book.BookingNo)
            {
                return true;
            }
        }
        return false;
    }
    else if (args == 1)
    {
        foreach (Booking book in books)
        {
            if (bookno == book.BookingNo)
            {
                book.Rate = nrate;
                return true;
            }
        }
        return false;
    }
    else
    {
        return false;
    }
}

string str = "Update Room Rate";
Console.WriteLine(str);
Console.WriteLine(new String('-',str.Length));
Console.Write("Enter Booking No: ");
int bookno = Convert.ToInt32(Console.ReadLine());
bool found = updateroomrate(bookno, '0', bookings, 0);
if (found)
{
    Console.WriteLine($"Current rate : {bookings[bookno - 1].Rate:F2}");
    Console.Write("Enter new rate: ");
    double newrate = Convert.ToDouble(Console.ReadLine());
    bool result = updateroomrate(bookno, newrate, bookings, 1);
    if (result)
    {
        Console.WriteLine("The new rate is updated successfully");
        displaybook(bookings);
    }
    else
    {
        Console.WriteLine("Error, please try again");
    }
}
else
{
    Console.WriteLine("Booking not found!");
    displaybook(bookings);
}