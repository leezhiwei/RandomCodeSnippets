use NP40Book;
-- Q1
select BranchNo, "Number of Members" = COUNT(MemberID) from Member group by BranchNo;
-- Q2
select ISBN, "Number of Copies" = COUNT(*) from BookCopy group by ISBN order by "Number of Copies" desc;
-- Q3
select ISBN, "Number of Copies" = COUNT(*) from BookCopy group by ISBN having COUNT(*) > 2 order by "Number of Copies" desc;
-- Q4
select BookCat, PublisherID, "Number of Books" = count(ISBN) from Book group by PublisherID, BookCat;
-- Q5
select BranchNo, SupervisorID,"Number of Female Staffs" = count(StaffID) from Staff where Gender = 'F' and SupervisorID is not null group by BranchNo, SupervisorID;
-- Q6
select Name as "Publisher", "Number of Books" = count(*) from Book join Publisher on Publisher.PublisherID = Book.PublisherID group by Name order by "Number of Books" desc;
-- Q7
select ISBN, CopyNo, DateOut from Loan where MemberID = (select MemberID from Member where Name = 'Kumar');
-- Q8
select Title, YearPublish from Book where ISBN in (select distinct ISBN from BookCopy where CopyNo >= 1);
-- Q9
select ISBN, Title from Book where ISBN not in (select ISBN from Loan);
-- Q10
select Name, Salary from Staff where Salary = (select max(Salary) from Staff);
-- Q11
select MemberID, Name, Gender from Member where MemberID in (select MemberID from Loan group by MemberID having count(LoanNo) > 5 );
-- Q12
select distinct Name from Staff where StaffID in (select SupervisorID from Staff) order by Name;
-- Q13
-- No, since the where clause does not allow for aggregate clauses like MAX or SUM