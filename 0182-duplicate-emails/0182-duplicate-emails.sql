SELECT email AS Email
FROM (
    SELECT email, count(email) AS cnt
    FROM Person
    GROUP BY email
    HAVING cnt > 1
) as subQuery