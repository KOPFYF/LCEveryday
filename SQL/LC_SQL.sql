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
(SELECT DISTINCT Score FROM Scores) S2 -- S2 like a dense_rank()
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

-- 185. Department Top Three Salaries(hard)
Select dep.Name as Department, emp.Name as Employee, emp.Salary 
from Department dep, Employee emp 
where emp.DepartmentId = dep.Id and 
(Select count(distinct Salary) From Employee where DepartmentId=dep.Id and Salary>emp.Salary) < 3；

select Dept.name as Department, Sub.name as Employee, Sub.salary as Salary from
(select *, 
 dense_rank() over (partition by departmentid order by salary desc) as rnk from employee) Sub
inner join Department Dept on Sub.departmentid = Dept.id
where rnk < 4；
----------------------------------- end ---------------------------------------

-- 196. Delete Duplicate Emails -----------------------------------------------
-- You can't specify target table 'Person' for update in FROM clause
DELETE FROM Person WHERE Id NOT IN
(SELECT * FROM (SELECT MIN(Id) AS Id FROM Person GROUP BY Email) p);

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email
AND p1.Id > p2.Id; -- which means p1 comes after p2
----------------------------------- end ---------------------------------------

-- 197, DATEDIFF(), TO_DAYS()

-- 569. Median Employee Salary(hard) ------------------------------------------
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

-- 570. Managers with at Least 5 Direct Reports
SELECT NAME FROM Employee
WHERE Id in
(SELECT ManagerId
FROM Employee 
GROUP BY ManagerId
HAVING COUNT(Id) >= 5)
----------------------------------- end ---------------------------------------

-- 574. Winning Candidate -----------------------------------------------------
select Name 
from Candidate c 
join Vote v on c.id = v.CandidateId
group by Name
order by count(CandidateId) desc
limit 1;
----------------------------------- end ---------------------------------------


-- 578. Get Highest Answer Rate Question
with tmp as (
select
    question_id,
    sum(case when answer_id is not Null then 1 else 0 end) / count(*) as rate
from survey_log
group by question_id)

select
question_id as survey_log
from tmp
where rate in (select max(rate) from tmp);
----------------------------------- end ---------------------------------------



-- 579. Find Cumulative Salary of an Employee
# A.month : 5 => B.month : 4, 3, 2
# A.month : 4 => B.month : 3, 2, 1
# A.month : 3 => B.month : 2, 1
# A.month : 2 => B.month : 1

SELECT   A.Id, MAX(B.Month) as Month, SUM(B.Salary) as Salary 
-- for A.month = 5 it will select max(4, 3, 2) or 4
FROM     Employee A, Employee B  -- cross join
WHERE    A.Id = B.Id AND B.Month BETWEEN (A.Month-3) AND (A.Month-1)
GROUP BY A.Id, A.Month
ORDER BY Id, Month DESC;

SELECT id, month, Salary FROM
(
SELECT  id, 
        month, 
    -- Every 3 months. ROWS 2 PRECEDING indicates the number of rows or values to precede the current row (1 + 2)
        SUM(salary) OVER(PARTITION BY id  ORDER BY month ROWS 2 PRECEDING) as Salary, 
        DENSE_RANK() OVER(PARTITION BY id ORDER by month DESC) month_no
FROM Employee
)  src
--  exclude the most recent month
where month_no > 1
ORDER BY id, month desc;
----------------------------------- end ---------------------------------------

-- 585. Investments in 2016
select sum(TIV_2016) TIV_2016
from insurance a
where 1 = (select count(*) from insurance b where a.LAT=b.LAT and a.LON=b.LON) 
and 1 < (select count(*) from insurance c where a.TIV_2015=c.TIV_2015);

SELECT SUM(insurance.TIV_2016) AS TIV_2016
FROM insurance
WHERE insurance.TIV_2015 IN -- meet the creteria #1
    (
       SELECT TIV_2015
        FROM insurance
        GROUP BY TIV_2015
        HAVING COUNT(*) > 1
        )
AND (LAT, LON) IN -- meet the creteria #2
    (
      SELECT LAT, LON -- trick to take the LAT and LON as a pair
      FROM insurance
      GROUP BY LAT , LON
      HAVING COUNT(*) = 1
);
----------------------------------- end ---------------------------------------


-- 597. Friend Requests I: Overall Acceptance Rate
SELECT IFNULL(ROUND(COUNT(DISTINCT requester_id, accepter_id) / 
       COUNT(DISTINCT sender_id, send_to_id), 2), 0.00) AS accept_rate
FROM RequestAccepted, FriendRequest;

-- follow-up1:Can you write a query to return the accept rate but for every month?
-- create a subquery which contains count, month, join each other with month and group by month so we can get the finally result.
select if(d.req = 0, 0.00, round(c.acp/d.req, 2)) as accept_rate, c.month from 
(select count(distinct requester_id, accepter_id) as acp, Month(accept_date) as month from request_accepted) c, 
(select count(distinct sender_id, send_to_id) as req, Month(request_date) as month from friend_request) d 
where c.month = d.month 
group by c.month;

-- follow-up2:How about the cumulative accept rate for every day?
-- sum up the case when ind is 'a', which means it belongs to accept table, divided by sum of ind is 'r', which means it belong to request table
select s.date1, ifnull(round(sum(case when t.ind = 'a' then t.cnt else 0 end)
              /sum(case when t.ind = 'r' then t.cnt else 0 end),2),0) 
from
-- get a table of all unique dates
(select distinct x.request_date as date1 from friend_request x
-- The reason here use union sicne we don't want duplicate date
union 
 select distinct y.accept_date as date1 from request_accepted y 
) s
## left join to make sure all dates are in the final output
left join 
## get a table of all dates, count of each days, ind to indicate which table it comes from
(select v.request_date as date1, count(*) as cnt,'r' as ind from friend_request v group by v.request_date
## The reason here use union all sicne union all will be faster
union all
select w.accept_date as date1, count(*) as cnt,'a' as ind from request_accepted w group by w.accept_date) t
## s.date1 >= t.date1, which for each reacord in s, it will join with all records earlier than it in t
on s.date1 >= t.date1
# group by s.date1 then we can get a cumulative result to that day
group by s.date1
order by s.date1
;
----------------------------------- end ---------------------------------------

-- 601. Human Traffic of Stadium
SELECT DISTINCT t1.* -- remove duplicate rows
FROM stadium t1, stadium t2, stadium t3
WHERE t1.people >= 100 AND t2.people >= 100 AND t3.people >= 100
AND(
  (t1.id - t2.id = 1 and t1.id - t3.id = 2) -- return id: 7,8
  OR (t2.id - t1.id = 1 and t2.id - t3.id = 2) -- return id: 6,7
  OR (t3.id - t2.id = 1 and t3.id - t1.id = 2) -- return id: 5,6
)
ORDER BY t1.visit_date;
----------------------------------- end ---------------------------------------

-- 602. Friend Requests II: Who Has the Most Friends
select id, count(*) as num from 
(
      (select requester_id id from request_accepted) 
      union all 
      (select accepter_id id from request_accepted)
) tb 
group by id order by num desc limit 1;
----------------------------------- end ---------------------------------------

-- 603. Consecutive Available Seats
select distinct A1.seat_id
from cinema A1, cinema A2
where A1.free = true and A2.free = true
and abs(A1.seat_id - A2.seat_id) = 1
order by A1.seat_id；
----------------------------------- end ---------------------------------------


-- 608. Tree Node
SELECT T.id,
  CASE WHEN isnull(T.p_id) THEN 'Root'
       WHEN T.id in (select T.p_id from tree T) THEN 'Inner'
       ELSE 'Leaf'
  END AS Type
FROM Tree T;
----------------------------------- end ---------------------------------------

-- 614. Second Degree Follower ------------------------------------------------
SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM follow f1
JOIN follow f2
ON f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower;
----------------------------------- end ---------------------------------------

-- 619. Biggest Single Number
SELECT MAX(a.num) as num 
FROM (
SELECT num
FROM my_numbers
GROUP BY num
HAVING COUNT(num) = 1) a
----------------------------------- end ---------------------------------------

-- 626. Exchange Seats

SELECT a.id, a.student
FROM
    (   SELECT id - 1 as id, student
        FROM seat -- even, -1
        WHERE id % 2 = 0
    UNION
        SELECT id + 1 as id, student
        FROM seat -- odd, + 1
        WHERE id % 2 = 1 AND id != (SELECT MAX(id) FROM seat)
    UNION 
        SELECT id, student
        FROM seat -- the last odd, fixed, no need to add 1 
        WHERE id % 2 = 1 AND id = (SELECT MAX(id) FROM seat)
    ) a
ORDER BY a.id;

select 
    (case 
    when mod(id, 2) != 0 and id != (select max(id) from seat) then id + 1
    when mod(id, 2) != 0 and id = (select max(id) from seat) then id
    else id - 1
    end) as id, 
    student from seat 
order by id asc;
----------------------------------- end ---------------------------------------

-- 627. Swap Salary
UPDATE salary SET sex = 
case 
    when sex = 'm' then 'f'
    else 'm'
end;

update salary set sex = char(211 - ascii(sex))；
update salary set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));
update salary set sex = CHAR(ASCII('f') + ASCII('m') - ASCII(sex));

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
----------------------------------- end ---------------------------------------

-- 1204. Last Person to Fit in the Elevator
SELECT person_name 
FROM (SELECT person_name, 
       SUM(weight) OVER (ORDER BY turn ASC) as acc_weight
FROM Queue) tmp
WHERE acc_weight <= 1000
ORDER BY acc_weight DESC LIMIT 1;

(select count(*) from friends group by activity order by 1 limit 1)
AND COUNT(*) <
(select count(*) from friends group by activity order by 1 desc limit 1);
----------------------------------- end ---------------------------------------

-- 1532. The Most Recent Three Orders
SELECT c.name AS customer_name, c.customer_id, order_id, order_date
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS row_num
    FROM orders) tmp
JOIN customers c
ON c.customer_id = tmp.customer_id
WHERE row_num <= 3
ORDER BY customer_name ASC, customer_id, order_date DESC
----------------------------------- end ---------------------------------------

-- 1517. Find Users With Valid E-mails
SELECT * FROM Users 
WHERE REGEXP_LIKE(mail, '^[A-Aa-z]+[A-Aa-z0-9\.\_\-]*@leetcode.com')
----------------------------------- end ---------------------------------------

-- 1454. Active Users
SELECT DISTINCT l1.id, A.name
FROM Logins l1
JOIN Logins l2
ON l1.id = l2.id AND DATEDIFF(l2.login_date, l1.login_date) BETWEEN 1 AND 4
JOIN Accounts A
ON l1.id = A.id
GROUP BY l1.id, l1.login_date
HAVING COUNT(DISTINCT l2.login_date) = 4;

WITH A AS
    (SELECT id, login_date, 
            LEAD(login_date,4) OVER(PARTITION BY id ORDER BY login_date) AS lead_date
    FROM (SELECT DISTINCT id, login_date FROM Logins) aa)
SELECT DISTINCT A.id, acc.name
FROM A
INNER JOIN Accounts acc
ON A.id = acc.id
WHERE DATEDIFF(A.lead_date, A.login_date) = 4
ORDER BY A.id;
----------------------------------- end ---------------------------------------


-- 1892. Page Recommendations II
-- Create a CTE with all friends list.
with friends as
(
    select user1_id as user_id, user2_id as friend from friendship
    union
    select user2_id as user_id, user1_id as friend from friendship
)

-- Use JOIN to get all friends liked page, then use LEFT JOIN to exclude pages was liked by user_id
select f.user_id, l1.page_id, count(l1.page_id) as friends_likes
from friends f
join Likes l1 on f.friend = l1.user_id
left join Likes l2 on f.user_id = l2.user_id and l1.page_id = l2.page_id 
where l2.page_id is null
group by f.user_id, l1.page_id;

----------------------------------- end ---------------------------------------

-- 1264. Page Recommendations
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (
    SELECT user2_id AS friend_id FROM Friendship WHERE user1_id = 1
    UNION
    SELECT user1_id AS friend_id FROM Friendship WHERE user2_id = 1) 
AND page_id NOT IN (
      SELECT page_id FROM Likes WHERE user_id = 1
    );

----------------------------------- end ---------------------------------------


-- 1934. Confirmation Rate
select s.user_id,
round(avg(case when c.action = 'confirmed' then 1.00 else 0.00 end), 2) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id;
----------------------------------- end ---------------------------------------


-- 1965. Employees With Missing Information
select * from
(select e.employee_id
from Employees e
left join Salaries s
on e.employee_id = s.employee_id 
where s.employee_id is null
union 
select s.employee_id
from Employees e
right join Salaries s
on e.employee_id = s.employee_id 
where e.employee_id is null) tmp
order by employee_id;
----------------------------------- end ---------------------------------------


-- 1949. Strong Friendship
# requirement: user1_id < user2_id
# soln 1, c1 and c2 has u1, find their common u2
with cte as(select user1_id,user2_id from friendship
            union 
            select user2_id,user1_id from friendship)
            
select c1.user1_id
      ,c2.user1_id as user2_id
	  ,count(*) as common_friend 
from cte as c1 
     join 
	 cte as c2
on c1.user1_id < c2.user1_id 
   and 
   c1.user2_id = c2.user2_id
where (c1.user1_id, c2.user1_id) in (select * from friendship)
group by 1,2
having count(*) >= 3;

# soln 2, f2 contains 
with f as (
    select user1_id, user2_id from friendship
    union all
    select user2_id as user1_id, user1_id as user2_id from friendship
)

select f1.user1_id, f1.user2_id, count(*) as common_friend 
from f f1
join f f2
on f1.user1_id = f2.user1_id # add user1's friend from f2 (f2.u2 is common with f3.u2)
join f f3
on f1.user2_id = f3.user1_id and f2.user2_id = f3.user2_id # add user2's friend
where f1.user1_id < f1.user2_id # dedup filter out pairs that user1_id > user2_id
group by f1.user1_id, f1.user2_id
having count(*) >= 3;
----------------------------------- end ---------------------------------------


-- 1972. First and Last Call On the Same Day
# rank() by call_time to get the first and last call, group by user and day
# having count(distinct recipient_id) = 1: make sure it's the same person
with tmp1 as (
    select caller_id as user_id, recipient_id, call_time from calls
    union all
    select recipient_id as user_id, caller_id as recipient_id, call_time from calls
),

tmp2 as (
    select user_id, recipient_id, date(call_time) as day,
        dense_rank() over (partition by user_id, date(call_time) order by call_time asc) as rn,
        dense_rank() over (partition by user_id, date(call_time) order by call_time desc) as rk
    from tmp1
)

select distinct user_id
from tmp2
where rn = 1 or rk = 1 
group by user_id, day
having count(distinct recipient_id) = 1;
----------------------------------- end ---------------------------------------


-- 1831. Maximum Transaction Each Day
# max(amount), where in
select transaction_id 
from Transactions
where (amount, date(day)) in
( select max(amount) as max_amt, date(day) as day1 
from Transactions group by date(day) ) 
order by transaction_id;

# window func, dense_rank
select transaction_id
from 
(select transaction_id, 
        dense_rank() over (partition by date(day) order by amount desc) as rk
from Transactions) as sub
where rk = 1
order by transaction_id;
----------------------------------- end ---------------------------------------
