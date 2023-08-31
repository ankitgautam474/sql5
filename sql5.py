SELECT S.Sname, O.Snum, COUNT(*) as NumOrders, MAX(O.Odate) as LatestOrderDate
FROM SalesPeople S
JOIN Orders O ON S.Snum = O.Snum
GROUP BY S.Sname, O.Snum;
