CREATE DATABASE SQLSyntaxTest;
USE SQLSyntaxTest
GO
CREATE TABLE CustInfo (CustID int not null, Name text not null, Age int not null, IsCitizen BIT not null);
INSERT INTO CustInfo VALUES (1,'Dan',17,1),(2,'Mike',16,1),(3,'Micheal',20,0),(4,'Dennis',22,1);
SELECT * FROM CustInfo;
ALTER Table CustInfo ADD DidPassExam BIT not null DEFAULT 1;
SELECT * FROM CustInfo;
UPDATE CustInfo SET DidPassExam = 1;
ALTER Table CustInfo ADD IsMale BIT not null DEFAULT 1;
INSERT INTO CustInfo VALUES (5,'Maria',29,0,1,0);
SELECT * FROM CustInfo;