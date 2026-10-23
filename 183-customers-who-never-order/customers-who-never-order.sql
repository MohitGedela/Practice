SELECT name AS Customers
FROM Customers a
WHERE NOT EXISTS (
    SELECT *
    FROM Orders b
    WHERE a.id = b.customerId   
) 