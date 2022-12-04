-- Practical 5
use master;
-- Q3
drop database if exists NewNP40Book;
create database NewNP40Book;
-- Q4
use NewNP40Book;
drop table if exists BookCategory;
create table BookCategory(BookCat char(2) primary key, Description varchar(max) not null);
-- Q5
drop table if exists Publisher;
create table Publisher(PublisherID int primary key, Name varchar(max) not null);
-- Q6
drop table if exists Book;
create table Book(ISBN char(10) primary key, Title varchar(max) not null, YearPublish char(4) not null, PublisherID int foreign key references Publisher(PublisherID), BookCat char(2) foreign key references BookCategory(BookCat));
-- Q7
use master;
insert into NewNP40Book.dbo.BookCategory select * from NP40Book.dbo.BookCategory;
insert into NewNP40Book.dbo.Publisher select * from NP40Book.dbo.Publisher;
insert into NewNP40Book.dbo.Book select * from NP40Book.dbo.Book;
-- Q8
use NewNP40Book;
insert into Book values('0385605196', 'Not the end of the world',2002,4,'F'),('0385605196','The Devil wears Prada',2003,4,'F');
-- Unable to insert duplicate primary key, due to primary key being unique and therefore a violation.
-- Q9
insert into Publisher values(9,'Pearson Prentice Hall');
insert into Book values('981244579X','Database',2003,9,'NF');
-- should insert publisher first, since it need the FK to be in the Publisher table first
-- Q10
update Publisher set Name = 'Happy Day' where PublisherID = 4;
-- Q11
update BookCategory set Description = 'Comedy' where BookCat = 'C';
-- Q12
update Book set PublisherID = (select PublisherID from Publisher where Name = 'Addison Wesley') where Title = 'Database Systems';
update Book set BookCat = 'NF' where Title = 'Database Systems';
-- Q13
update Publisher set Name = 'Heinz' from Publisher join Book on Book.PublisherID = Publisher.PublisherID where Book.Title = 'The Best of Catherine Lim';
-- Q14
delete from Book where ISBN = '0072126949';
-- Q15
delete from Book where ISBN = '981244579X';
delete from Publisher where PublisherID = 9;
-- Should remove from Book first, as this is where the FK is referenced, thus removing any references before deleting the actual record.