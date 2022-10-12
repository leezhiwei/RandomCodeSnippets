CREATE DATABASE SQLSyntaxTest; -- create the test database
USE SQLSyntaxTest; -- use the created database
CREATE TABLE CustInfo (CustID int not null, Name text not null, Age int not null, IsCitizen bool not null); -- create columns
INSERT INTO CustInfo VALUES (1,'Dan',17,true),(2,'Mike',16,true),(3,'Micheal',20,false),(4,'Dennis',22,true); -- Insert first value
SELECT * FROM CustInfo; -- Show initial table with values and columns
ALTER TABLE CustInfo ADD DidBuyThings BOOL not null DEFAULT true; -- Add new column
SELECT * FROM CustInfo; -- show the table with the new column
UPDATE CustInfo SET DidBuyThings = false where CustID % 2 != 0; -- only update table where customer id is odd.
ALTER Table CustInfo ADD IsMale BOOL not null DEFAULT true; -- add new column
INSERT INTO CustInfo VALUES (5,'Maria',29,false,true,false); -- add new value
SELECT * FROM CustInfo; -- show end table
