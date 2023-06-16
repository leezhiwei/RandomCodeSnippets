USE MokeSellDBAsg1;
SELECT SellerID, CommunicationRank, MemberName, MemberDOB, MemberEmail, MemberMobile, Listing.ListDesc FROM Review INNER JOIN Offer ON Offer.OfferID = Review.OfferID INNER JOIN Listing ON Listing.ListingID = Offer.ListingID INNER JOIN Member ON Member.MemberID = Listing.SellerID WHERE CommunicationRank = (SELECT MAX(CommunicationRank) AS "Ranking for Communication" FROM Review);
SELECT Team.TeamID, COUNT(*) AS "Number of Feedback", TeamName, s2.StaffName FROM FeedBack 
INNER JOIN Staff ON Staff.StaffID = FeedBack.StaffID 
INNER JOIN Team ON Staff.TeamID = Team.TeamID
INNER JOIN Staff s2 ON s2.StaffID = Team.TeamLeaderID
GROUP BY Team.TeamID, TeamName, s2.StaffName
HAVING COUNT(*) = (SELECT MAX("Number of Feedback") AS "Maximum Number of followers" 
FROM
(SELECT COUNT(*) AS "Number of Feedback" 
FROM FeedBack 
INNER JOIN Staff ON Staff.StaffID = FeedBack.StaffID 
INNER JOIN Team ON Staff.TeamID = Team.TeamID 
GROUP BY Team.TeamID) as sub);
SELECT CASE
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 18 AND 20 THEN 'Below 20'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 20 AND 30 THEN 'Between 20 and 30'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 30 AND 40 THEN 'Between 30 and 40'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 40 AND 50 THEN 'Between 40 and 50'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 50 AND 60 THEN 'Between 50 and 60'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) BETWEEN 60 AND 70 THEN 'Between 60 and 70'
  WHEN DATEDIFF(year, MemberDOB, GETDATE()) > 70 THEN 'Above 70'
END AS Age_Range, DATEDIFF(year, MemberDOB, GETDATE()) AS "Age", COUNT(*) AS "Number of Bumps" FROM BumpOrder 
INNER JOIN Member ON Member.MemberID = BumpOrder.SellerID GROUP BY DATEDIFF(year, MemberDOB, GETDATE())
HAVING COUNT(*) = 
(SELECT MAX("Number of Bumps") AS "Maximum Bumps" 
FROM
(SELECT COUNT(*) AS "Number of Bumps" 
FROM BumpOrder 
INNER JOIN Member
ON Member.MemberID = BumpOrder.SellerID
GROUP BY Member.MemberID) as sub);