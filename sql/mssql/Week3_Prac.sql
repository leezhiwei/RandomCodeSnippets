use NP40Book;
-- Q1
select Book.ISBN, CopyNo, RentalRate from BookCopy join Book on Book.ISBN = BookCopy.ISBN;
-- Q2
select ISBN, Title, Category = Description from Book join BookCategory on BookCategory.BookCat = Book.BookCat order by Title; 
-- Q3
select Staff.BranchNo, Address, "Manager's Name" = Name from Staff join Branch on Branch.BranchNo = Staff.BranchNo where SupervisorID is null;
-- Q4
select Staff.StaffID, Staff.Name, Staff.DateJoin from Staff join Staff as Staff2 on Staff.SupervisorID = Staff2.StaffID where Staff2.Name = 'May May';
-- Q5
select Book.ISBN, Title, Loan.DateOut from Book join Loan on Book.ISBN = Loan.ISBN join Member on Member.MemberID = Loan.MemberID where Member.Name = 'Kumar';
-- Q6
select Book.ISBN, Title, Name from Book join BookAuthor on BookAuthor.ISBN = Book.ISBN join Author on Author.AuthorID = BookAuthor.AuthorID order by Title;
-- Q7
select count(LoanNo) as "Number of Loans", sum(RentalRate) as "Total Rental Rate" from Loan join Member on Member.MemberID = Loan.MemberID where Member.Name = 'Jeremy Law';
-- Q8
select distinct Staff.Name from Staff join Staff as Staff2 on Staff.StaffID = Staff2.SupervisorID order by Staff.Name;
-- Q9
select ISBN, Title, YearPublish from Book join Publisher on Book.PublisherID = Publisher.PublisherID join BookCategory on BookCategory.BookCat = Book.BookCat where Publisher.Name = 'Arrow Books' and BookCategory.Description = 'Fiction' order by YearPublish;
-- Q10
select Staff.StaffID, Staff.Name, Staff.DateJoin, datediff(year, Staff.DateJoin, getdate()) as "Years in Service" from Staff join Staff as Staff2 on Staff.SupervisorID = Staff2.StaffID where Staff2.Name = 'May May' and datediff(year, Staff.DateJoin, getdate()) < 10;
-- Q11
select LoanNo, ISBN, Name, DateOut, RentalRate from Loan join Member on Member.MemberID = Loan.MemberID;
-- Q12
select Loan.ISBN, CopyNo, DateOut from Loan join Book on Loan.ISBN = Book.ISBN where Book.Title = 'Stuart Little';
-- Q13
select ISBN, Title, YearPublish from Book join Publisher on Book.PublisherID = Publisher.PublisherID where Publisher.Name = 'Pan Books';
-- Q14
select Loan.MemberID, Name, DateDue, DateReturn from Loan join Member on Loan.MemberID = Member.MemberID where DateReturn > DateDue order by DateReturn desc;