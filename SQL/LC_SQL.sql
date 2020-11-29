-- 176. Second Highest Salary -------------------------------------------------
/* MySQL: */
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
----------------------------------- end ---------------------------------------

-- 177. Nth Highest Salary ----------------------------------------------------
/* MySQL: */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END
----------------------------------- end ---------------------------------------

-- 178. Rank Scores -----------------------------------------------------------
/* MySQL: Cross Join */
SELECT S.Score, COUNT(S2.Score) AS `Rank`
FROM Scores S,
(SELECT DISTINCT Score FROM Scores) S2
WHERE S.Score <= S2.Score
GROUP BY S.Id 
ORDER BY S.Score DESC;

SELECT Score,
	DENSE_RANK() OVER (ORDER BY Score DESC) as `Rank`
FROM Scores;

/* MySQL server: Write your T-SQL query statement below */
SELECT Score,
	DENSE_RANK() OVER (ORDER BY Score DESC) as Rank
FROM Scores;
----------------------------------- end ---------------------------------------


-- 180. Consecutive Numbers ---------------------------------------------------
/* MySQL: Cross Join */
select distinct a1.Num as ConsecutiveNums
from Logs a1, Logs a2, Logs a3
where a1.id = a2.id - 1 and a2.id = a3.id - 1 and a1.Num = a2.Num and a2.Num = a3.Num
----------------------------------- end ---------------------------------------

-- 181. Employees Earning More Than Their Managers ----------------------------
select E1.Name as Employee
from Employee as E1, Employee as E2 
where E1.ManagerId = E2.Id and E1.Salary > E2.Salary
----------------------------------- end ---------------------------------------

-- 184. Department Highest Salary ---------------------------------------------
-- cross join 3 tables
SELECT D.Name AS Department, E.Name AS Employee, E.Salary
FROM Employee E,
(SELECT DepartmentId, Name, Max(Salary) AS maxSalary FROM Employee GROUP BY DepartmentId) T,
Department D
WHERE E.DepartmentId = T.DepartmentId
AND E.Salary = T.maxSalary
AND E.DepartmentId = D.Id;

-- using subquery
SELECT D.Name AS Department ,E.Name AS Employee ,E.Salary 
FROM Employee E, Department D 
WHERE E.DepartmentId = D.id 
  AND (DepartmentId, Salary) IN 
  (SELECT DepartmentId, MAX(Salary) AS maxSalary FROM Employee GROUP BY DepartmentId);
----------------------------------- end ---------------------------------------

-- 196. Delete Duplicate Emails -----------------------------------------------
-- You can't specify target table 'Person' for update in FROM clause
DELETE FROM Person WHERE Id NOT IN
(SELECT * FROM (SELECT MIN(Id) AS Id FROM Person GROUP BY Email) p)
----------------------------------- end ---------------------------------------

-- 569. Median Employee Salary ------------------------------------------------
SELECT
  id,
  Company,
  Salary
FROM Employee e
WHERE 1 >= ABS((SELECT COUNT(*) FROM Employee e1 WHERE e.company = e1.company AND e.Salary >= e1.Salary) -
           (SELECT COUNT(*) FROM Employee e2 WHERE e.company = e2.company AND e.Salary <= e2.Salary)) 
GROUP BY Company, Salary;  

SELECT Id, Company, Salary
FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
FROM Employee) AS temp
WHERE ABS(RN_ASC - RN_DESC) BETWEEN 0 AND 1
GROUP BY Company, Salary;
----------------------------------- end ---------------------------------------

-- 574. Winning Candidate -----------------------------------------------------
select Name 
from Candidate c 
join Vote v on c.id = v.CandidateId
group by Name
order by count(CandidateId) desc
limit 1;
----------------------------------- end ---------------------------------------

-- 614. Second Degree Follower ------------------------------------------------
SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM follow f1
JOIN follow f2
ON f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower;
----------------------------------- end ---------------------------------------

-- 1045. Customers Who Bought All Products ------------------------------------
select customer_id
from customer c
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from product)
----------------------------------- end ---------------------------------------

-- 1076. Project Employees II -------------------------------------------------
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(project_id) = 
(SELECT COUNT(project_id) 
 FROM Project
 GROUP BY project_id
 ORDER BY COUNT(project_id) DESC
 LIMIT 1)

with a as (select project_id, count(employee_id) as ct 
  from Project as p 
  group by project_id)
  
select project_id 
  from a 
  where a.ct = (select max(ct) from a)
----------------------------------- end ---------------------------------------

-- 1077. Project Employees III ------------------------------------------------
select p.project_id, e.employee_id
from Project p
left join Employee e
on p.employee_id = e.employee_id
where (p.project_id, e.experience_years) in
(SELECT p.project_id, max(e.experience_years)
from project as p
inner join employee as e 
on e.employee_id = p.employee_id
group by project_id);

select t.project_id, t.employee_id
from
    (select project_id,
    p.employee_id,
    rank() over(partition by project_id order by experience_years desc) as rank
    from Project p join Employee e
    on p.employee_id = e.employee_id) t
where t.rank = 1;

with employee_experience as (
    select p.project_id, p.employee_id,
    rank() over(partition by p.project_id order by experience_years desc) as rank
    from Project p join Employee e
    on p.employee_id = e.employee_id)

select project_id, employee_id
from employee_experience
where rank = 1;
----------------------------------- end ---------------------------------------

-- 1164. Product Price at a Given Date ----------------------------------------
SELECT distinct a.product_id, ifnull(temp.new_price, 10) as price 
FROM products as a
LEFT JOIN
(SELECT * 
FROM products 
WHERE (product_id, change_date) in 
 (select product_id, max(change_date) # find the price for the most recent change
  from products 
  where change_date <= "2019-08-16" 
  group by product_id)
) as temp
on a.product_id = temp.product_id; 

----------------------------------- end ---------------------------------------

-- 1179. Reformat Department Table --------------------------------------------
select id, 
	sum(case when month = 'jan' then revenue else null end) as Jan_Revenue,
	sum(case when month = 'feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'may' then revenue else null end) as May_Revenue,
	sum(case when month = 'jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from department
group by id
order by id;
----------------------------------- end ---------------------------------------

-- 1285. Find the Start and End Number of Continuous Ranges -------------------
SELECT min(log_id) as start_id, max(log_id) as end_id
FROM
(SELECT log_id, 
        ROW_NUMBER() OVER(ORDER BY log_id) as num
FROM Logs) a
GROUP BY log_id - num;
----------------------------------- end ---------------------------------------


-- 1303. Find the Team Size
SELECT a.employee_id, b.team_size
FROM Employee a
JOIN 
(SELECT team_id, COUNT(employee_id) AS team_size
FROM Employee
GROUP BY team_id) b
ON a.team_id = b.team_id;

select employee_id, count(*) over(partition by team_id) as team_size
from employee;
----------------------------------- end ---------------------------------------


-- 1322. Ads Performance
SELECT ad_id, 
IFNULL(ROUND(AVG(CASE WHEN action = 'Clicked' THEN 1
                         WHEN action = 'Viewed' THEN 0
                         ELSE NULL END)*100, 2), 0) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;

select ad_id, 
ifnull(round(sum(case when action = 'Clicked' then 1 else 0 end) / 
             sum(case when action = 'Clicked' or action = 'Viewed' then 1 else 0 end) * 100, 2), 0) as ctr
from Ads
group by ad_id
order by ctr desc, ad_id asc;
----------------------------------- end ---------------------------------------

-- 1398. Customers Who Bought Products A and B but Not C
select customer_id, customer_name
from Customers
where customer_id in
(select customer_id from Orders where product_name = 'A')
and customer_id in
(select customer_id from Orders where product_name = 'B')
and customer_id not in
(select customer_id from Orders where product_name = 'C')
----------------------------------- end ---------------------------------------

-- 1667. Fix Names in a Table
SELECT user_id,
       CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM Users
ORDER BY user_id;
----------------------------------- end ---------------------------------------

-- 1421. NPV Queries
SELECT q.id, q.year, IFNULL(n.npv, 0) AS npv
FROM Queries q
LEFT JOIN NPV n
ON q.id = n.id 
AND q.year = n.year;

select q.id, q.year, coalesce(n.npv, 0) as npv
from npv n right join queries q
on n.id = q.id and n.year = q.year;



