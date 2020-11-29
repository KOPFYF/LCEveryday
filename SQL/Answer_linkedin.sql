#1 MoM Percent Change
WITH tmp as
(SELECT
	DATE_TRUNC('month', date) as month_timestamp,
	COUNT(DISTINCT user_id) mau
 FROM logins
 GROUP BY DATE_TRUNC('month', date)
)

SELECT 
a.month_timestamp pre_month, a.mau pre_mau,
b.month_timestamp cur_month, b.mau cur_mau,
ROUND(100.0 * (b.mau - a.mau) / a.mau, 2)) AS percent_change
FROM tmp a
JOIN tmp b
ON MONTH(b.month_timestamp) - MONTH(a.month_timestamp) = 1 

#2 Tree Structure Labeling
SELECT T.id,
  CASE WHEN isnull(T.p_id) THEN 'ROOT'
  	   WHEN T.id in (select T.p_id from tree T) THEN 'INNER'
  	   ELSE 'LEAF'
  END AS Type
FROM Tree T

WITH join_table AS
(
 SELECT cur.node, cur.parent, COUNT(next.node) AS num_children
 FROM tree cur
 LEFT JOIN
 tree next 
 ON (next.parent = cur.node)
 GROUP BY cur.node, cur.parent)

SELECT node,
 CASE WHEN parent IS NULL THEN "Root"
      WHEN num_children = 0 THEN "Leaf"
      ELSE "Inner"
 END AS label
FROM join_table

#3 Retain Users Per Month
# Part 1, gets the number of retained users per month
# initial solution, self join
SELECT 
DATE_TRUNC('month', a.date) month_timestamp, 
COUNT(DISTINCT a.user_id) AS retained_user_count
FROM tmp a
JOIN tmp b
ON DATE_TRUNC('month', a.date) = DATE_TRUNC('month', b.date) + interval '1 month'
AND a.user_id = b.user_id
GROUP BY month_timestamp

# dedup first
WITH tmp as
(SELECT
	DATE_TRUNC('month', date) as month_timestamp,
	user_id
 FROM logins
 GROUP BY month_timestamp
)

SELECT 
a.month_timestamp pre_month, 
COUNT(a.user_id) AS retained_user_count
FROM tmp a
LEFT JOIN tmp b
ON a.month_timestamp = b.month_timestamp - interval '1 month'
AND a.user_id=b.user_id

# Part 2, find many users last month did not come back this month. i.e. the number of churned users.
SELECT 
DATE_TRUNC('month', a.date) month_timestamp, 
COUNT(DISTINCT b.user_id) AS churned_users
FROM tmp a
FULL OUTER JOIN tmp b
ON DATE_TRUNC('month', a.date) = DATE_TRUNC('month', b.date)
AND a.user_id=b.user_id
WHERE a.user_id is NULL
GROUP BY month_timestamp

# Part 3, the number of active users this month who have been reactivated — 
# in other words, users who have churned but this month they became active again
???
SELECT DATE_TRUNC('month', a.date) month_timestamp,
COUNT(DISTINCT a.user_id) reactivated_users,
/*
* At least in the flavors of SQL I have used, you
don't need to
* include the columns used in HAVING in the SELECT
statement.
* I have written them out for clarity here.
*/
MAX(DATE_TRUNC('month', b.date)) most_recent_active_previously
FROM logins a
JOIN logins b 
ON a.user_id = b.user_id
AND DATE_TRUNC('month', a.date) > DATE_TRUNC('month', b.date)
GROUP BY DATE_TRUNC('month', a.date)
HAVING month_timestamp > most_recent_active_previously + interval '1 month'

#4. Cumulative Sums, 
# self join
SELECT a.date date,
SUM(b.cash_flow) AS cumulative_cf
FROM transactions a
JOIN transactions b
ON a.date >= b.date
GROUP BY date
ORDER BY date ASC
# window function
SELECT date,
SUM(cash_flow) OVER(ORDER BY date ASC) AS cumulative_cf
FROM transactions 
ORDER BY date ASC

#5. Rolling AVG
#self join
SELECT a.date date,
AVG(b.cash_flow) AS avg_cf
FROM transactions a
JOIN transactions b
ON a.date >= b.date and a.date <= b.date + interval '6 days'
GROUP BY date
ORDER BY date ASC

#6. Multiple join, email average response time
SELECT a.id,
MIN(b.timestamp) - a.timestamp as time_to_respond
FROM emails a
JOIN emails b
ON b.subject = a.subject
AND a.to = b.from
AND a.from = b.to
AND a.timestamp < b.timestamp
WHERE a.to = 'zach@g.com'
GROUP BY a.id


-------------------- WINDOW FUNCTION ---------------------
#1: Get the ID with the highest value
# subquery
SELECT s.empno FROM salaries s
INNER JOIN 
(SELECT MAX(salary) max_salary FROM salaries) ms
ON s.salary = ms.max_salary;
 
# window, RANK()
SELECT sr.empno FROM
(SELECT empno, RANK() OVER (ORDER BY salary DESC) rnk
 FROM salaries) sr
WHERE rnk = 1;

#2. AVG salary, rank per department 
# part 1
SELECT empno, 
ROUND(AVG(salary), 0) OVER (PARTITION BY depname) avg_salary
FROM salaries;
# part 2
SELECT *, 
RANK() OVER (PARTITION BY depname) rnk
FROM salaries;

-------------------- OTHERS ---------------------
#1. Histograms
WITH bin_label AS
(SELECT session_id, 
	    FLOOR(length_seconds/5) as bin_label
 FROM sessions)
SELECT CONCATENTATE(STR(bin_label*5),'-',STR(bin_label*5+5) bucket,
       COUNT(DISTINCT session_id)) COUNT
GROUP BY bin_label
ORDER BY bin_label

#2. CROSS JOIN(multiple parts)
# part 1, Write a query to get the pairs of states with total streaming amounts within 1000 of each other.
SELECT a.state as state_a,
	   b.state as state_b
FROM state_streams a
CROSS JOIN state_streams b
WHERE ABS(a.total_streams - b.total_streams) < 1000
AND a.state <> b.state
-- or without explicitly specifying a join
SELECT a.state as state_a,
	   b.state as state_b
FROM state_streams a,
     state_streams b
WHERE ABS(a.total_streams - b.total_streams) < 1000
AND a.state <> b.state

# part 2, remove dup from part 1 (the pair NC and SC should only appear)
SELECT a.state as state_a,
	   b.state as state_b
FROM state_streams a,
     state_streams b
WHERE ABS(a.total_streams - b.total_streams) < 1000
AND a.state > b.state

#3. Advancing Counting
# Write a query to count the number of users in each class such that any user who has label a and b gets
# sorted into b, any user with just a gets sorted into a and any user with just b gets into b.
WITH usr_b_sum AS
(
 SELECT user,
	    SUM(CASE WHEN class = 'b' THEN 1 ELSE 0 END) num_b
 FROM table
 GROUP BY user
),
 	
 usr_class_label AS
(
 SELECT user,
 		CASE WHEN num_b > 0 THEN 'b' ELSE 'a' END class
 FROM usr_b_sum
)

SELECT class,
 	   COUNT(DISTINCT user) count
FROM usr_class_label
GROUP BY class
ORDER BY class ASC

-- soln 2 --
WITH max_class AS 
(
SELECT user,
 	   MAX(class) as class
FROM table
GROUP BY user
)

SELECT class, COUNT(user)
FROM max_class
GROUP BY class










