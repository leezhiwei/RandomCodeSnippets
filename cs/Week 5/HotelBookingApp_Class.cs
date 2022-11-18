namespace HotelBookingApp
{
    internal class Booking
    {
        private int bookingNo;
        private string name;
        private DateTime dateIn;
        private DateTime dateOut;
        private double rate;

        public int BookingNo {get; set;}
        public string Name {get; set;}
        public DateTime DateIn {get; set;}
        public DateTime DateOut {get; set;}
        public double Rate { get; set; }
        public Booking()
        {
            BookingNo = 0;
            Name = "";
            dateIn = DateTime.Now;
            dateOut = DateTime.Now.AddDays(1);
        }
        public Booking(int no, string na, DateTime indt, DateTime outdt, double ra)
        {
            BookingNo = no;
            Name = na;
            DateIn = indt;
            DateOut = outdt;
            Rate = ra;
        }
        public int CalculateDuration(Booking book)
        {
            TimeSpan duration = book.DateOut - book.DateIn;
            return duration.Days;

        }
        public double CalculateCharge(Booking booking, double rate)
        {
            int duration = CalculateDuration(booking);
            return rate * duration;
        }
        public override string ToString()
        {
            return $"{BookingNo}, {Name}, {DateIn.ToString()}, {DateOut.ToString()}, {rate}";
        }
    }
}
