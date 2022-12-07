CREATE DATABASE SQLSyntaxTest; -- create db
USE SQLSyntaxTest -- use the db
GO
CREATE TABLE CustInfo (CustID int not null primary key, Name varchar(max) not null, Age int not null, IsCitizen BIT not null); -- create the table
INSERT INTO CustInfo VALUES (1,'Dan',17,1),(2,'Mike',16,1),(3,'Micheal',20,0),(4,'Dennis',22,1); -- insert value
SELECT * FROM CustInfo; -- show initial table
ALTER Table CustInfo ADD DidBuyThings BIT not null DEFAULT 1; -- add column 
SELECT * FROM CustInfo; -- show the current state of table
UPDATE CustInfo SET DidBuyThings = 0 where CustID %2 != 0; -- update the column
ALTER Table CustInfo ADD IsMale BIT not null DEFAULT 1; -- add column
INSERT INTO CustInfo VALUES (5,'Maria',29,0,1,0); -- insert new values
SELECT * FROM CustInfo; -- show final state