use SQLSyntaxTest;
drop table if exists OrderInfo;
drop table if exists ItemInfo;
drop trigger if exists inserted_orders;
drop trigger if exists updated_orders;
create table ItemInfo (ItemCode int not null, ItemName nvarchar(4000) not null, UnitPrice decimal(10,2) not null, Description nvarchar(4000) not null, primary key (ItemCode));
create table OrderInfo (OrderID int not null, CustID int not null, ItemCode int not null, Quantity int not null, TotalValue decimal(10,2) not null default 0, foreign key (CustID) references CustInfo(CustID), foreign key (ItemCode) references ItemInfo(ItemCode), primary key (OrderID));
create trigger inserted_orders before insert on OrderInfo
for each row
	set NEW.TotalValue = (select UnitPrice from ItemInfo where ItemCode = NEW.ItemCode) * NEW.Quantity;
create trigger updated_orders before update on OrderInfo
for each row
	set NEW.TotalValue = (select UnitPrice from ItemInfo where ItemCode = NEW.ItemCode) * NEW.Quantity;
insert into ItemInfo values (1,N'烤面包机',35.00,N'品牌：烁宁烤盘 材质：压铸铝额定功率：600W 烤盘尺寸：135X108X25mm 产地：中国大陆发货地：浙江省 3C认证证书编号：2019010712240120'), 
(2, 'Google Pixel 6 Pro', 1048.59, '6.71 inches, LTPO AMOLED, 1440 x 3120 pixels, Corning Gorilla Glass Victus 128GB Storage, 12GB RAM Android 12, Google Tensor (5 nm), Octa-core (2x2.80 GHz Cortex-X1 & 2x2.25 GHz Cortex-A76 & 4x1.80 GHz Cortex-A55) 50 MP, f/1.9, 26mm (wide), 1/1.31", 1.2µm, omnidirectional PDAF, Laser AF, OIS, 48 MP, f/3.5, 104mm (telephoto), 1/2", 0.8µm, PDAF, OIS, 4x optical zoom, 12 MP, f/2.2, 114˚ (ultrawide), 1.25µm, Front, 11.1 MP, f/2.2, 20mm (ultrawide), 1.22µm'),
(3, 'Lenovo E14 Gen 4', 1346.28, 'Stylish, high-performance 14″ business laptop Up to Windows 11 Pro Powered by up to 12th Gen Intel® Core™ i7 processors Enhanced security & durability, weighs from just 1.59kg Plenty of DDR5 memory & SSD storage, optional dual SSD Dolby® Audio™ with Harman® speakers for superb audio Optional fingerprint reader & FHD hybrid IR camera');
insert into OrderInfo(OrderID, CustID, ItemCode, Quantity) values (1, 2, 1, 3), (2, 3, 3, 22), (3, 3, 2,23),(4, 4, 2, 5),(5,1,1,3);
select * from OrderInfo;
select * from ItemInfo;