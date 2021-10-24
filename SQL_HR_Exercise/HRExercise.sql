-- USE thist DB
USE HR_DB;

-- Find Employees with the lowest 3 salaries
SELECT TOP 3 
	salary 
From 
	employees
ORDER BY
	salary;

-- Find the Employee with the 2nd Highest Salary whose phone number begins with 515
SELECT 
	salary,
	phone_number
FROM
	employees
WHERE 
	phone_number lIKE('515%')
ORDER BY
	salary DESC
OFFSET 1 ROWS
FETCH NEXT 1 ROWS ONLY;

-- Find the name, salary, and hire date of all employees hired before 1995 and a salary over $10,000
SELECT 
	first_name,
	last_name,
	salary,
	hire_date
FROM
	employees
WHERE
	hire_date < '1995-01-01' AND
	salary > 10000;

-- Get all the unique salaries in the employee table. 
SELECT DISTINCT
	salary 
FROM
	employees;

-- List each unique salary and how many people make that salary
SELECT
	salary,
	COUNT(*) 'Employees who make this salary'
FROM
	employees
GROUP BY
	salary;

-- Group employees by department id, find the average salary of each department. Order them from lowest salary to highest.
SELECT
	department_id,
	AVG(salary) 'AVG Salary'
FROM
	employees
GROUP BY
	department_id
ORDER BY
	'AVG Salary';

-- Find all the employees hired between 1995 - 1997
	-- Order the employed by their department id and hire date
		-- Using OVER & PARTITION BY, list the average salary for their department next to each row
SELECT 
	department_id,
	hire_date,
	AVG(salary) OVER (PARTITION BY department_id) 'AVG SALARY'
FROM
	employees
WHERE
	hire_date BETWEEN '1995-01-01' AND '1997-12-31'
ORDER BY
	department_id, hire_date;


--Select the average salary of an employee per department, round to next whole number, only include even salaries.
SELECT
	department_id,
	CEILING(AVG(salary)) 'AVG Salary'
FROM
	employees
GROUP BY
	department_id
HAVING
	CEILING(AVG(salary))%2 = 0;
