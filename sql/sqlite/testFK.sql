create table CustInfo (CustID int not null primary key, Name varchar not null, Age int not null);
create table ItemInfo (ItemCode int not null primary key, ItemName varchar not null, UnitPrice decimal(10,2) not null, StockAmount int not null);
create table OrderInfo (CustID int not null, OrderID int not null primary key, ItemCode int not null, Quantity int not null, foreign key (CustID) references CustInfo(CustID), foreign key(ItemCode) references ItemInfo (ItemCode));
insert into ItemInfo values (1, 'Pixel 6', 999.99, 100), (2, 'Lenovo E14 Gen 3', 1022.55, 6), (3, 'Toaster', 35.32, 55);
insert into CustInfo values (1, 'Dan', 21), (2, 'Jon', 23), (3, 'Matt', 45);
insert into OrderInfo values (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 2, 3), (2, 4, 1, 4), (3, 5, 2, 5), (1, 6, 3, 6);
select OrderInfo.OrderID, ItemInfo.ItemName, (ItemInfo.UnitPrice * OrderInfo.Quantity) 'TotalPrice' from ItemInfo join OrderInfo on OrderInfo.ItemCode = ItemInfo.ItemCode join CustInfo on CustInfo.CustID = OrderInfo.CustID where CustInfo.Name = 'Matt';

