-- Write a SQL query to fetch all the columns from a table named Employees.

Select *
From Employees


-- Filtering Rows: Write a SQL query to fetch all the employees whose salary is greater than 50000.


Select *
From Employees
where Salary>50000

-- Ordering Results: Write a SQL query to fetch all employees, ordered by their last name in ascending order
Select *
From Employees
Order By LastName ASC


-- Aggregate Function (COUNT): Write a SQL query to count the number of employees in the Employees table
Select Count(*)
From Employees


-- Using DISTINCT: Write a SQL query to fetch unique job titles from the Employees table
Select DISTINCT(titles)
From Employees

-- JOIN Operation: Write a SQL query to fetch employee names along with their department names. Assume you have Employees and Departments tables

Select e.name,d.name
From Employees e
JOIN Departments d
On e.department_id=d.department_id

-- Group By: Write a SQL query to fetch the number of employees in each department
Select department,count(*) as numberofemployees
From Employees 
Group by department

-- HAVING Clause: Write a SQL query to fetch departments having more than 10 employees.

Select department
From Employees
Group by department
having count(*)>10

-- Subquery: Write a SQL query to fetch the employees whose salary is above the average salary
Select name
From Employees
where Salary > (Select AVG(Salary)
From Employees)


-- Updating Data: Write a SQL query to increase the salary of all employees by 10%.
UPDATE employee
Set salary=salary*1.1


-- Nested Subqueries: Write a SQL query to fetch employees who work in a department where the average salary is above 60000.

Select name
from employee
where department_id in (
    Select department_id
    From Employees
    Group by department_id
    having AVG(salary)>60000
)



--  Write a SQL query to delete employees who have not logged in for more than a year. Assume a column LastLoginDate.


delete From Employees
where LastLoginDate<DATE_SUB(NOW(), INTERVAL 1 YEAR);







