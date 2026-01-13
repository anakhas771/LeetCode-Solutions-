# Write your MySQL query statement below
select distinct email as Email from Person GROUP BY email HAVING COUNT(email) > 1;