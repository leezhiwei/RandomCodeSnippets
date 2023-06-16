-- Team 6 SQL Creation Script
-- Lee Zhi Wei, Lim Jia Xian, Peter Liau, Ye Qi Yang, Cayden Xie
-- MD5 Hash 364dff6b6f199071ab11db22ac0dab65
-- SHA256 Hash 12754042d7ce985e40cfdf3bb7c458aa31a4a4d7166bc5b2f80ccbb23d4e5090
-- Last Modified 27 Jan 2023

USE master;

DROP DATABASE IF EXISTS MokeSellDBAsg1;
CREATE DATABASE MokeSellDBAsg1;

GO
USE MokeSellDBAsg1;

DROP TABLE IF EXISTS Award;
CREATE TABLE Award (AwardID INT PRIMARY KEY IDENTITY(1,1), AwardName VARCHAR(120) NOT NULL, AwardAmt SMALLMONEY CHECK (AwardAmt > 0) NOT NULL);

DROP TABLE IF EXISTS Bump;
CREATE TABLE Bump (BumpID INT PRIMARY KEY IDENTITY(1,1), BumpDesc VARCHAR(999), BumpPrice SMALLMONEY CHECK (BumpPrice > 0) NOT NULL );

DROP TABLE IF EXISTS Category;
CREATE TABLE Category (CatID INT PRIMARY KEY IDENTITY(1,1), CatDesc VARCHAR(999) NOT NULL);

DROP TABLE IF EXISTS FeedbkCat;
CREATE TABLE FeedbkCat (FbkCatID INT PRIMARY KEY IDENTITY(1,1), FbkCatDesc VARCHAR(999) NOT NULL);

DROP TABLE IF EXISTS Member;
CREATE TABLE Member (MemberID INT PRIMARY KEY IDENTITY(1,1), MemberName NVARCHAR(100) NOT NULL, MemberDOB DATETIME NOT NULL, MemberEmail VARCHAR(100), MemberMobile VARCHAR(8) CHECK ((MemberMobile LIKE '8%' OR MemberMobile LIKE '9%' OR MemberMobile LIKE '6%') AND LEN(MemberMobile) = 8), MemberDateJoined DATETIME NOT NULL, City VARCHAR(100), CONSTRAINT DateConst CHECK(MemberDOB < MemberDateJoined), CONSTRAINT AgeLimit CHECK(DATEDIFF(YEAR, MemberDOB, GETDATE()) >= 18));

DROP TABLE IF EXISTS Buyer;
CREATE TABLE Buyer (BuyerID INT FOREIGN KEY REFERENCES Member(MemberID) PRIMARY KEY);

DROP TABLE IF EXISTS Seller;
CREATE TABLE Seller (SellerID INT FOREIGN KEY REFERENCES Member (MemberID) PRIMARY KEY);

DROP TABLE IF EXISTS SubCategory;
CREATE TABLE SubCategory (SubCatID INT PRIMARY KEY IDENTITY(1,1), SubCatDesc VARCHAR(999) NOT NULL, CatID INT FOREIGN KEY REFERENCES Category(CatID) NOT NULL);

DROP TABLE IF EXISTS Listing;
CREATE TABLE Listing (ListingID INT PRIMARY KEY IDENTITY(1,1), ListDesc VARCHAR(1000), ListDateTime DATETIME NOT NULL CHECK (ListDateTime <= GETDATE() AND YEAR(ListDateTime) >= 2000), ListPrice MONEY CHECK (ListPrice >= 0) NOT NULL, ListStatus VARCHAR(9) CHECK (ListStatus = 'Available' OR ListStatus = 'Sold' OR ListStatus = 'Inactive') NOT NULL, SellerID INT FOREIGN KEY REFERENCES Seller(SellerID) NOT NULL, SubCatID INT FOREIGN KEY REFERENCES SubCategory(SubCatID) NOT NULL);

DROP TABLE IF EXISTS Follower;
CREATE TABLE Follower (MemberID INT FOREIGN KEY REFERENCES Member(MemberID) NOT NULL, FollowerID INT FOREIGN KEY REFERENCES Member(MemberID) NOT NULL, DateStarted DATETIME NOT NULL CHECK ((GETDATE() >= DateStarted) AND (YEAR(DateStarted) >= 2000)), CONSTRAINT MemberCombKey_PK PRIMARY KEY (MemberID,FollowerID));

DROP TABLE IF EXISTS Likes;
CREATE TABLE Likes (BuyerID INT FOREIGN KEY REFERENCES Buyer(BuyerID) NOT NULL, ListingID INT FOREIGN KEY REFERENCES Listing(ListingID) NOT NULL, DateLiked DATETIME NOT NULL, CONSTRAINT Like_PK PRIMARY KEY (BuyerID, ListingID));

DROP TABLE IF EXISTS ListingPhoto;
CREATE TABLE ListingPhoto (ListingID INT FOREIGN KEY REFERENCES Listing(ListingID) NOT NULL, Photo VARCHAR(100) NOT NULL, CONSTRAINT Photo_PK PRIMARY KEY (ListingID, Photo));

DROP TABLE IF EXISTS Offer;
CREATE TABLE Offer (OfferID INT PRIMARY KEY IDENTITY(1,1), BuyerID INT FOREIGN KEY REFERENCES Buyer(BuyerID) NOT NULL, ListingID INT FOREIGN KEY REFERENCES Listing(ListingID) NOT NULL, OfferPrice MONEY CHECK (OfferPrice >= 0) NOT NULL, OfferStatus VARCHAR(9) CHECK (OfferStatus = 'Submitted' OR OfferStatus = 'Pending' OR OfferStatus = 'Accepted' OR OfferStatus = 'Rejected' OR OfferStatus = 'Completed') NOT NULL, OfferDate DATETIME CHECK ((GETDATE() >= OfferDate) AND (YEAR(OfferDate) >= 2000)) NOT NULL);

DROP TABLE IF EXISTS Chat;
CREATE TABLE Chat (ChatID INT PRIMARY KEY IDENTITY(1,1), BuyerID INT FOREIGN KEY REFERENCES Buyer(BuyerID) NOT NULL, ListingID INT FOREIGN KEY REFERENCES Listing(ListingID) NOT NULL);

DROP TABLE IF EXISTS ChatMsg;
CREATE TABLE ChatMsg (ChatID INT FOREIGN KEY REFERENCES Chat(ChatID) NOT NULL, MsgSN VARCHAR(99) NOT NULL, MsgDateTime DATETIME2 CHECK ((GETDATE() >= MsgDateTime) AND (YEAR(MsgDateTime) >= 2000)) NOT NULL, Originator VARCHAR(6) CHECK (Originator = 'Seller' OR Originator = 'Buyer') NOT NULL, Msg VARCHAR(1000) NOT NULL, CONSTRAINT PK_ChatMsg PRIMARY KEY (ChatID, MsgSN));

DROP TABLE IF EXISTS Staff;
CREATE TABLE Staff (StaffID INT PRIMARY KEY IDENTITY(1,1), StaffName NVARCHAR(100) NOT NULL, StaffMobile CHAR(8) CHECK ((StaffMobile LIKE '8%' OR StaffMobile LIKE '9%' OR StaffMobile LIKE '6%') AND LEN(StaffMobile) = 8), StaffDateJoined DATETIME NOT NULL, CONSTRAINT YearCheck CHECK ((YEAR(StaffDateJoined) >= 2000) AND (GETDATE() >= StaffDateJoined)));

DROP TABLE IF EXISTS Team;
CREATE TABLE Team (TeamID INT PRIMARY KEY IDENTITY(1,1), TeamName NVARCHAR(100) NOT NULL, TeamLeaderID INT FOREIGN KEY REFERENCES Staff(StaffID) NOT NULL);

ALTER TABLE Staff ADD TeamID INT FOREIGN KEY REFERENCES Team(TeamID);

DROP TABLE IF EXISTS Win;
CREATE TABLE Win (AwardID INT FOREIGN KEY REFERENCES Award(AwardID) NOT NULL, TeamID INT FOREIGN KEY REFERENCES Team(TeamID) NOT NULL, DateAwarded DATETIME NOT NULL CHECK ((GETDATE() >= DateAwarded) AND (YEAR(DateAwarded) >= 2000)), CONSTRAINT Win_PK PRIMARY KEY (AwardID, TeamID, DateAwarded));

DROP TABLE IF EXISTS Review;
CREATE TABLE Review (ReviewID INT PRIMARY KEY IDENTITY(1,1), OfferID INT FOREIGN KEY REFERENCES Offer(OfferID) NOT NULL, MemberType VARCHAR(6) CHECK (MemberType = 'Seller' OR MemberType = 'Buyer') NOT NULL, ReviewDate DATETIME CHECK ((GETDATE() >= ReviewDate) AND (YEAR(ReviewDate) >= 2000)) NOT NULL, ItemRank TINYINT CHECK ((ItemRank BETWEEN 1 AND 5) AND (ItemRank > 0)), DeliveryRank TINYINT CHECK ((DeliveryRank BETWEEN 1 AND 5) AND (DeliveryRank > 0)), CommunicationRank TINYINT CHECK ((CommunicationRank BETWEEN 1 AND 5) AND (CommunicationRank > 0)), Comment VARCHAR(999));

DROP TABLE IF EXISTS FeedBack;
CREATE TABLE FeedBack (FbkID INT PRIMARY KEY IDENTITY(1,1), ByMemberID INT FOREIGN KEY REFERENCES Member(MemberID) NOT NULL, FbkCatID INT FOREIGN KEY REFERENCES FeedbkCat(FbkCatID) NOT NULL, FbkDesc VARCHAR(999) NOT NULL, FbkDateTime DATETIME CHECK ((GETDATE() >= FbkDateTime) AND (YEAR(FbkDateTime) >= 2000)) NOT NULL, FbkStatus VARCHAR(19) CHECK (FbkStatus = 'Pending' OR FbkStatus = 'Receiving Attention' OR FbkStatus = 'Completed') NOT NULL, SatisfactionRank TINYINT CHECK ((SatisfactionRank BETWEEN 1 AND 5) AND (SatisfactionRank > 0)), OnMemberID INT FOREIGN KEY REFERENCES Member(MemberID) NOT NULL, StaffID INT FOREIGN KEY REFERENCES Staff(StaffID) NOT NULL);

DROP TABLE IF EXISTS BumpOrder;
CREATE TABLE BumpOrder (BumpOrderID INT PRIMARY KEY IDENTITY(1,1), PurchaseDate DATETIME CHECK ((GETDATE() >= PurchaseDate) AND (YEAR(PurchaseDate) >= 2000)) NOT NULL, SellerID INT FOREIGN KEY REFERENCES Seller(SellerID) NOT NULL, BumpID INT FOREIGN KEY REFERENCES Bump(BumpID) NOT NULL, ListingID INT FOREIGN KEY REFERENCES Listing(ListingID) NOT NULL);

-- Inserting all values

insert into Award (AwardName, AwardAmt) values ('CEO List: Best Employees 2020 Award', '$3920.27');
insert into Award (AwardName, AwardAmt) values ('Best Team Award 2013', '$7461.35');
insert into Award (AwardName, AwardAmt) values ('Best Team Award 2021', '$7390.24');
insert into Award (AwardName, AwardAmt) values ('Most Hardworking Staff Award', '$1000');
insert into Award (AwardName, AwardAmt) values ('Best Team Award 2020', '$8042.19');


insert into Bump (BumpDesc, BumpPrice) values ('Try to sell my listing fast.', '$20.06');
insert into Bump (BumpDesc, BumpPrice) values ('My listing has quite less views.', '$24.65');
insert into Bump (BumpDesc, BumpPrice) values ('Hope this will help my listing.', '$16.30');
insert into Bump (BumpDesc, BumpPrice) values ('Last 5 item, selling fast.', '$12.24');
insert into Bump (BumpDesc, BumpPrice) values ('Buy 3 laptops get 1 free.', '$20.20');
insert into Bump (BumpDesc, BumpPrice) values ('New product from New Zealand/Australia.', '$17.69');
insert into Bump (BumpDesc, BumpPrice) values ('Brand new stocks! Selling fast.', '$13.27');
insert into Bump (BumpDesc, BumpPrice) values ('The one and only, MightyMug.', '$14.63');
insert into Bump (BumpDesc, BumpPrice) values ('Brand new Sony TV 20% off.', '$22.90');
insert into Bump (BumpDesc, BumpPrice) values ('Hello, brand new hand-phone for sale.', '$15.83');
insert into Bump (BumpDesc, BumpPrice) values ('Best deal, do visit my profile.', '$14.75');
insert into Bump (BumpDesc, BumpPrice) values (null, '$20.67');

insert into Category (CatDesc) values ('Food');
insert into Category (CatDesc) values ('Computers & Tech');
insert into Category (CatDesc) values ('Furniture');
insert into Category (CatDesc) values ('Books');
insert into Category (CatDesc) values ('Dress');
insert into Category (CatDesc) values ('Games');
insert into Category (CatDesc) values ('Property');

insert into FeedbkCat (FbkCatDesc) values ('Technical Issues');
insert into FeedbkCat (FbkCatDesc) values ('Scammed');
insert into FeedbkCat (FbkCatDesc) values ('Late Delivery');
insert into FeedbkCat (FbkCatDesc) values ('Fast Delivery');
insert into FeedbkCat (FbkCatDesc) values ('Good Products');

insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Sissie Kilshall', '3/26/1999', 'skilshall0@arizona.edu', '82333416', '12/31/2020', 'Puerto Boyacá');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Meade Copley', '1/13/1954', 'mcopley1@usnews.com', '93945764', '7/28/2020', 'Onan Ganjang Satu');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Baily Dykins', '11/2/1980', 'bdykins2@dedecms.com', '86219694', '10/30/2012', 'Maño');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Vivia Farnie', '6/17/1954', 'vfarnie3@marriott.com', '68889714', '10/28/2016', 'Huangtugang');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('April Carnilian', '6/21/1977', 'acarnilian4@feedburner.com', '99274772', '10/9/2003', 'Ishimbay');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Bowie Georger', '3/17/1976', 'bgeorger5@stanford.edu', '67136052', '11/3/2015', 'Titay');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Deane Brok', '10/26/1975', 'dbrok6@ox.ac.uk', '67354862', '11/23/2002', 'Figueiras');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Emeline Gebbe', '10/23/1971', 'egebbe7@blogspot.com', '90266312', '5/9/2012', 'Nungga');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Helen Cullinan', '12/16/1972', 'hcullinan8@google.nl', '98785094', '3/1/2019', 'Magrath');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Rancell Mil', '8/13/1982', 'rmil9@nyu.edu', '69614630', '1/6/2006', 'Qianguo');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Karola Tipperton', '11/11/1997', 'ktippertona@github.com', '95872345', '11/5/2015', 'Albuquerque');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Jeanna Petchell', '10/1/1960', null, null, '7/13/2002', null);
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Sheila-kathryn Sahlstrom', '8/24/1959', 'ssahlstromc@columbia.edu', '92956625', '8/4/2019', 'Lundazi');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Emalee Greser', '10/10/1962', 'egreserd@prweb.com', '96813858', '7/31/2020', 'Los Cóndores');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Arvin Mattis', '1/30/2000', 'amattise@mac.com', '85241043', '3/29/2018', 'Lido');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Maddie Vyvyan', '4/20/1979', 'mvyvyanf@huffingtonpost.com', '96321569', '9/2/2007', 'Fonte Boa');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Jerrilee McCafferky', '3/1/2000', 'jmccafferkyg@g.co', '99671813', '1/27/2021', 'Andaray');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Janis Telfer', '12/19/1955', 'jtelferh@stanford.edu', '98131554', '1/25/2005', 'Baucau');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Obadiah Buckmaster', '2/28/1982', 'obuckmasteri@harvard.edu', '63459047', '12/24/2001', 'Foumban');
insert into Member (MemberName, MemberDOB, MemberEmail, MemberMobile, MemberDateJoined, City) values ('Kristan Cattroll', '5/1/1950', 'kcattrollj@sbwire.com', '90234729', '8/24/2011', 'Abakan');

insert into Buyer (BuyerID) values (1);
insert into Buyer (BuyerID) values (2);
insert into Buyer (BuyerID) values (3);
insert into Buyer (BuyerID) values (4);
insert into Buyer (BuyerID) values (5);
insert into Buyer (BuyerID) values (6);
insert into Buyer (BuyerID) values (7);
insert into Buyer (BuyerID) values (8);
insert into Buyer (BuyerID) values (9);
insert into Buyer (BuyerID) values (10);

insert into Seller (SellerID) values (11);
insert into Seller (SellerID) values (12);
insert into Seller (SellerID) values (13);
insert into Seller (SellerID) values (14);
insert into Seller (SellerID) values (15);
insert into Seller (SellerID) values (16);
insert into Seller (SellerID) values (17);
insert into Seller (SellerID) values (18);
insert into Seller (SellerID) values (19);
insert into Seller (SellerID) values (20);

insert into SubCategory (SubCatDesc, CatID) values ('Snacks', 1);
insert into SubCategory (SubCatDesc, CatID) values ('Drinks', 1);
insert into SubCategory (SubCatDesc, CatID) values ('Processors', 2);
insert into SubCategory (SubCatDesc, CatID) values ('Desktops', 2);
insert into SubCategory (SubCatDesc, CatID) values ('AAA Game', 6);
insert into SubCategory (SubCatDesc, CatID) values ('Sofa', 3);
insert into SubCategory (SubCatDesc, CatID) values ('Fiction', 4);
insert into SubCategory (SubCatDesc, CatID) values ('Non-Fiction', 4);
insert into SubCategory (SubCatDesc, CatID) values ('Wedding Gown', 5);
insert into SubCategory (SubCatDesc, CatID) values ('Instant Food', 1);
insert into SubCategory (SubCatDesc, CatID) values ('Condominum', 7);


insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('Mashed Potatoes', '11/1/2019', '$9.07', 'Inactive', 18, 10);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values (null, '6/12/2016', '$1734.52', 'Inactive', 11, 4);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('Call of Duty IDK 6', '7/1/2004', '$100.88', 'Available', 12, 5);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('Intel Core i7 7700k', '8/31/2022', '$439.35', 'Sold', 13, 3);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('Wedding Gown FOR SALE!!!', '10/5/2016', '$2880.59', 'Sold', 19, 9);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('100 PLUS, pack of 50.', '12/25/2022', '$62.39', 'Sold', 17, 2);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('Deep exploration of space: A story.', '3/26/2017', '$8.05', 'Inactive', 20, 8);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('New DIY Desktop, with Intel Core i7 4700k, and GTX 1080 Ti', '12/31/2018', '$6542.42', 'Available', 15, 4);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('New IN-STOCK Real Leather Sofa, now made with Premium Wagyu Cow Skin.', '7/9/2013', '$650.06', 'Available', 16, 6);
insert into Listing (ListDesc, ListDateTime, ListPrice, ListStatus, SellerID, SubCatID) values ('New premium chips, 1000 stock, imported from Switzerland, gone through Malaysia.', '9/21/2022', '$5.95', 'Sold', 14, 1);

insert into Follower (MemberID, DateStarted, FollowerID) values (12, '5/16/2022', 1);
insert into Follower (MemberID, DateStarted, FollowerID) values (4, '10/6/2021', 3);
insert into Follower (MemberID, DateStarted, FollowerID) values (4, '3/31/2022', 20);
insert into Follower (MemberID, DateStarted, FollowerID) values (16, '1/2/2023', 19);
insert into Follower (MemberID, DateStarted, FollowerID) values (20, '3/19/2022', 2);
insert into Follower (MemberID, DateStarted, FollowerID) values (5, '10/16/2021', 7);
insert into Follower (MemberID, DateStarted, FollowerID) values (3, '12/17/2022', 20);
insert into Follower (MemberID, DateStarted, FollowerID) values (6, '11/29/2022', 5);
insert into Follower (MemberID, DateStarted, FollowerID) values (1, '11/23/2022', 15);
insert into Follower (MemberID, DateStarted, FollowerID) values (18, '9/1/2022', 6);
insert into Follower (MemberID, DateStarted, FollowerID) values (13, '8/6/2021', 9);
insert into Follower (MemberID, DateStarted, FollowerID) values (1, '8/31/2021', 16);


insert into Likes (BuyerID, ListingID, DateLiked) values (10, 9, '12/5/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (7, 1, '11/24/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (3, 8, '12/11/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (2, 4, '10/31/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (9, 1, '10/29/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (10, 3, '12/10/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (9, 2, '12/28/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (3, 3, '1/10/2023');
insert into Likes (BuyerID, ListingID, DateLiked) values (10, 1, '11/24/2022');
insert into Likes (BuyerID, ListingID, DateLiked) values (5, 9, '1/12/2023');

insert into ListingPhoto (ListingID, Photo) values (10, 'PhotoID4143');
insert into ListingPhoto (ListingID, Photo) values (2, 'PhotoID8827');
insert into ListingPhoto (ListingID, Photo) values (4, 'PhotoID9260');
insert into ListingPhoto (ListingID, Photo) values (1, 'PhotoID8419');
insert into ListingPhoto (ListingID, Photo) values (5, 'PhotoID8639');
insert into ListingPhoto (ListingID, Photo) values (8, 'PhotoID3494');
insert into ListingPhoto (ListingID, Photo) values (8, 'PhotoID1278');
insert into ListingPhoto (ListingID, Photo) values (8, 'PhotoID4170');
insert into ListingPhoto (ListingID, Photo) values (5, 'PhotoID5210');
insert into ListingPhoto (ListingID, Photo) values (4, 'PhotoID1411');

insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (5, 3, '$110', 'Completed', '8/16/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (7, 8, '$6000', 'Completed', '9/25/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (4, 9, '$500', 'Rejected', '8/16/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (9, 10, '$5.95', 'Completed', '12/10/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (5, 5, '$2900', 'Accepted', '8/20/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (5, 2, '$1700', 'Accepted', '3/26/2022');
insert into Offer (BuyerID, ListingID, OfferPrice, OfferStatus, OfferDate) values (1, 9, '$700', 'Completed', '5/27/2022');

insert into Chat (BuyerID, ListingID) values (1, 4);
insert into Chat (BuyerID, ListingID) values (9, 7);
insert into Chat (BuyerID, ListingID) values (1, 3);
insert into Chat (BuyerID, ListingID) values (10, 2);
insert into Chat (BuyerID, ListingID) values (4, 9);

insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (1, 1, '12/30/2022', 'Buyer', 'Hi, I want to buy this intel processor.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (1, 2, '12/31/2022', 'Seller', 'This is Limited-Edition one.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (2, 1, '6/17/2018', 'Seller', 'This is very interesting Book. Want to buy?');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (2, 2, '7/20/2018', 'Buyer', 'Sorry, not interested.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (3, 1, '2/6/2020', 'Buyer', 'Hi, I want to buy this.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (3, 2, '5/8/2020', 'Seller', 'Sorry, this is old listing, sold already.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (4, 1, '4/14/2021', 'Buyer', 'Sorry, what are you selling?');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (4, 2, '5/21/2022', 'Seller', 'Some old desktops.');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (5, 1, '5/20/2019', 'Seller', 'This sofa is quite good quality, Interested?');
insert into ChatMsg (ChatID, MsgSN, MsgDateTime, Originator, Msg) values (5, 3, '5/20/2020', 'Buyer', 'Sorry. Unable to afford.');

insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Thaddeus Rippingall', null, '2021-08-12 03:09:07');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Thibaud Ruggiero', null, '2000-01-19 23:30:21');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Annabella Vittery', '99628470', '2010-08-30 02:49:44');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Annemarie Duckitt', '68486376', '2013-11-02 03:17:49');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Jamaal Iacomini', '62922775', '2020-04-15 09:35:27');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Denys Sartain', '98801503', '2019-07-22 07:17:19');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Kirbee Matthiae', '92030035', '2001-03-04 02:07:05');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Augustin Pelerin', '86277926', '2011-06-13 14:21:41');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Cynthie Lars', '97367276', '2001-05-10 19:35:16');
insert into Staff (StaffName, StaffMobile, StaffDateJoined) values ('Jerrylee Jonczyk', '88796573', '2009-06-03 03:11:41');

insert into Team (TeamName, TeamLeaderID) values ('Team Best', 1);
insert into Team (TeamName, TeamLeaderID) values ('Team Super-Marketing!', 3);
insert into Team (TeamName, TeamLeaderID) values ('Team Freedom', 5);
insert into Team (TeamName, TeamLeaderID) values ('Team Soar', 7);
insert into Team (TeamName, TeamLeaderID) values ('Team Guitar', 9);

UPDATE Staff SET TeamID = 1 WHERE StaffID = 1;
UPDATE Staff SET TeamID = 1 WHERE StaffID = 2;
UPDATE Staff SET TeamID = 2 WHERE StaffID = 3;
UPDATE Staff SET TeamID = 2 WHERE StaffID = 4;
UPDATE Staff SET TeamID = 3 WHERE StaffID = 5;
UPDATE Staff SET TeamID = 3 WHERE StaffID = 6;
UPDATE Staff SET TeamID = 4 WHERE StaffID = 7;
UPDATE Staff SET TeamID = 4 WHERE StaffID = 8;
UPDATE Staff SET TeamID = 5 WHERE StaffID = 9;
UPDATE Staff SET TeamID = 5 WHERE StaffID = 10;


insert into Win (AwardID, TeamID, DateAwarded) values (1, 3, '12/15/2020');
insert into Win (AwardID, TeamID, DateAwarded) values (2, 2, '12/2/2013');
insert into Win (AwardID, TeamID, DateAwarded) values (3, 3, '5/17/2021');
insert into Win (AwardID, TeamID, DateAwarded) values (4, 3, '12/19/2022');
insert into Win (AwardID, TeamID, DateAwarded) values (5, 4, '3/7/2020');

insert into Review (OfferID, MemberType, ReviewDate, ItemRank, DeliveryRank, CommunicationRank, Comment) values (1, 'Buyer', '1/10/2023', 4, 5, 5, 'Nice service, great job.');
insert into Review (OfferID, MemberType, ReviewDate, ItemRank, DeliveryRank, CommunicationRank, Comment) values (2, 'Seller', '1/15/2023', 4, 5, 1, 'Good product, buyer rude.');
insert into Review (OfferID, MemberType, ReviewDate, ItemRank, DeliveryRank, CommunicationRank, Comment) values (3, 'Seller', '1/6/2023', 4, 3, 4, 'Thing is OK, not tooo shabby.');
insert into Review (OfferID, MemberType, ReviewDate, ItemRank, DeliveryRank, CommunicationRank, Comment) values (4, 'Buyer', '1/15/2023', 3, 2, 1, 'Worst experience with seller.');
insert into Review (OfferID, MemberType, ReviewDate, ItemRank, DeliveryRank, CommunicationRank, Comment) values (5, 'Seller', '1/3/2023', 4, 2, 4, 'Good Service, with helpful buyer.');

insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (1, 5, 'Product in good condiiton.', '11/6/2022', 'Completed', 3, 7, 7);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (10, 5, 'Very good and useful products.', '11/26/2021', 'Completed', 5, 7, 4);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (4, 2, 'This is such a scam, I will complain it until it shut down!!', '2/21/2020', 'Pending', 3, 4, 3);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (8, 3, 'Uncle taking tour around Singapore is it? Product arrive 1 year later..', '6/1/2021', 'Completed', 1, 2, 4);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (9, 1, 'This MokeSell ah, make me lost all credit card details, live savings gone... Funny ah.', '3/23/2020', 'Completed', 1, 10, 6);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (3, 4, 'The moment I click order, I heard doorbell, what??? So fast.', '5/2/2021', 'Completed', 3, 7, 7);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (9, 4, 'I swear to god, I love this. It arrived from the back of a pickup-truck. Auntie driving truck sia.', '1/26/2022', 'Completed', 3, 3, 2);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (3, 5, 'Good product, will love to buy again.', '4/18/2021', 'Pending', 5, 8, 5);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (5, 1, 'App crashed and stopped multiple times. Not good impression...', '10/4/2021', 'Receiving Attention', 4, 2, 2);
insert into FeedBack (ByMemberID, FbkCatID, FbkDesc, FbkDateTime, FbkStatus, SatisfactionRank, OnMemberID, StaffID) values (4, 4, 'Bought a new screwdriver to fix my bicycle to go cycling, product arrived on time for me to join my friends to cycle. Thanks a lot. Ironically the uncle came on bicycle..', '6/10/2022', 'Receiving Attention', 1, 2, 2);

insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('12/25/2021', 15, 1, 3);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('8/24/2021', 17, 2, 9);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('10/9/2021', 18, 3, 4);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('12/5/2021', 14, 4, 1);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('6/30/2022', 18, 5, 3);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('1/14/2021', 16, 6, 8);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('11/15/2021', 14, 7, 6);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('9/30/2021', 15, 8, 1);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('3/23/2022', 20, 9, 6);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('7/27/2021', 13, 10, 2);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('9/3/2022', 19, 11, 1);
insert into BumpOrder (PurchaseDate, SellerID, BumpID, ListingID) values ('1/29/2021', 14, 12, 9);