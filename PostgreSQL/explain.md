
explain in postgres

a diagnostic command used to display the execution plan that the database optimizer chooses for a specific query.

---
wfdbtest=# explain select * from users limit 1;
                            QUERY PLAN                            
------------------------------------------------------------------
 Limit  (cost=0.00..0.03 rows=1 width=299)
   ->  Seq Scan on users  (cost=0.00..101.87 rows=2987 width=299)
(2 rows)

---

`Seq Scan` go to heap and fetch everything .. parallel scanning to get everything

`cost` 2 numbers 
1st: mili seconds to fetch the first result (row)
2nd: total time it will take to fetch the all data (approximate)

`rows`: number of estimated rows
`width`: sum of all bytes that a row on average takes