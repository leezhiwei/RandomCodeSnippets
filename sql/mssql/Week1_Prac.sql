use NP40Book;
-- Q1
select * from Staff;
-- Q2
select * from Book;
-- Q3
select StaffID, Name, Gender from Staff;
-- Q4
select ISBN, Title, PublisherID, BookCat from Book;
-- Q5
select SupervisorID from Staff;
-- Q6
select distinct SupervisorID from Staff;
-- Q7
select ISBN, CopyNo, RentalRate, NewRentalRate = RentalRate * 0.98 from BookCopy;
-- Q8
select * from Staff order by Name;
-- Q9
select * from Staff order by Name desc;
-- Q10
select BranchNo, Name, Salary from Staff order by BranchNo, Name;
-- Q11
select * from Member where BranchNo = 1;
-- Q12
select * from Book where BookCat = 'C';
-- Q13
select * from Member where BranchNo = 1 or BranchNo = 2;
-- Q14
select * from Book where (BookCat = 'C' or BookCat = 'F') and YearPublish > 2000;
-- Q15
select * from BookCopy where Status = 'D' and RentalRate > 5;
-- Q16
select * from Member where DateJoin between '1 Jan 2020' and '31 Dec 2020';
-- Q17
select * from Staff where DOB not between '1 Jan 1994' and '30 Jun 1996' order by DOB;
-- Q18
select * from Book where BookCat in ('C', 'F');
-- Q19
select * from Member where BranchNo in (1,2,3);
-- Q20
select * from Member where Name like 'Tan%';
-- Q21
select * from Book where Title like 'Database%';
-- Q22
select * from Book where Title like '%Database';
-- Q23
select * from Staff where SupervisorID is NULL;
-- Q24
select * from Book where BookCat != 'C' and BookCat != 'F' or BookCat is NULL order by BookCat, YearPublish desc;
select * from Book where BookCat not in ('C', 'F') or BookCat is NULL order by BookCat, YearPublish desc;
-- Q25
select BranchNo from Member;
-- Q26
select distinct	BranchNo from Member;
-- Q27
select StaffID, Name, Salary, NewSalary = Salary * 1.10 from Staff;
-- Q28
select StaffID, ContactNo from StaffContact order by StaffID;
-- Q29
select Name, Salary from Staff order by Salary desc;
-- Q30
select * from BookCopy order by DateIn desc;
-- Q31
select * from Book where BookCat = 'C' or BookCat = 'F';
-- Q32
select * from Member where (BranchNo = 1 or BranchNo = 2) and DateJoin > '31 Dec 2019';
-- Q33
select * from Staff where Gender = 'F' and Salary > 1500;
-- Q34
select * from Loan where DateOut between '1 Dec 2020' and '31 Jan 2021';
-- Q35
select * from Member where Name like '%Kim%';
-- Q36
select * from Book where BookCat is NULL;
-- Q37
select * from Staff where SupervisorID is not NULL order by SupervisorID;
-- Q38
select * from Member where Address like '%Street%' order by Name;
-- Q39
select * from Staff where (BranchNo = 1 or BranchNo = 3) and SupervisorID is NULL;
select * from Staff where BranchNo in (1,3) and SupervisorID is NULL;
-- Q40
select Name, Address, ContactNo from Member where DateJoin < '01 Jan 2020' and EmailAddr is NULL;
-- Q41
select * from BookCategory where Description = 'Fiction'; -- Since the BookCat has only has 2 absolute values "C" or "F" it is better to use =
-- Q42
select * from Book where YearPublish not like '199%';
select * from Book where YearPublish > 1999 or YearPublish < 1990;