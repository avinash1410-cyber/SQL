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





