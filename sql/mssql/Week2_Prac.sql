use NP40Book;
-- Q1(a)
select getdate();
-- Q1(b)
select month(getdate());
-- Q1(c)
select format(getdate(),'dddd dd MMM yyyy');
-- Q1(d)
select year(getdate());
-- Q1(e)
select day(getdate());
-- Q2
select MemberID,Name,DateJoin,'Years of Membership' = datediff(year,DateJoin,getdate()) from Member order by 'Years of Membership';
-- Q3
select LoanNo, ISBN, CopyNo, MemberID, [Number of days Overdue] = datediff(day, DateDue, DateReturn) from Loan where DateReturn is not null and datediff(day, DateDue, DateReturn) > 1 order by [Number of days Overdue] desc;
-- Q4
select StaffID, Name, Gender, DOB from Staff where month(DOB) = 2 order by Name;
-- Q5
select COUNT(*) as 'Number of Staff' from Staff;
-- Q6
select count(SupervisorID) from Staff;
-- Q7
select count(distinct SupervisorID) as 'Number of Supervisors' from Staff;
-- Q8
select count(*) as 'Members with email addresses' from Member where EmailAddr is not null;
-- Q9
select count(*) as 'Members without email addresses' from Member where EmailAddr is null;
-- Q10
select min(RentalRate) from BookCopy;
-- Q11
select 'Number of Loan' = count(*), 'Total Rental Income' = sum(RentalRate) from Loan where year(DateOut) = 2020;
-- Q12
select 'Number of Staff' = count(*), 'Total Annual Salary Payout' = sum(Salary) * 12 from Staff;
-- Q13
select LoanNo, 'Old DateDue' = DateDue, 'New DateDue' = 10 + DateDue from Loan order by 'New DateDue';
-- Q14
select Name, 'Email Address' = ISNULL(EmailAddr, 'Email Address Not Available') from Member order by Name;
-- Q15
select Name, Address, ContactNo from Member where year(DateJoin) < 2020 and EmailAddr is null;