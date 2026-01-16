# Write your MySQL query statement below
SELECT c.name AS Customers
from Customers c
Left join 
Orders o
On c.id=customerId
where customerId is null