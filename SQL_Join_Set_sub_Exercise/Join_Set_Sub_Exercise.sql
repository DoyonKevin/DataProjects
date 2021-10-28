USE HR_DB;

-- Select the first name, last name, job title, and department name for every employee using a join
SELECT
	first_name, last_name, j.job_title, department_name
FROM
	employees e
LEFT JOIN
	departments d
ON
	e.department_id = d.department_id
LEFT JOIN
	jobs j
ON
	j.job_id = e.job_id;
-- Select the first name, last name, and email of all the employees who have a dependant using a join and then using a subquery
SELECT
	e1.first_name,e1.last_name,e1.email
FROM
	employees e1
INNER JOIN
	dependents d2
ON
	e1.employee_id = d2.employee_id
WHERE
	e1.employee_id IN (
	SELECT
		employee_id
	FROM
		dependents
	);
-- Create a query that selects the city/province and state from the locations table and the number of employees in each of those locations ordered from highest to lowest
SELECT
	city, state_province, COUNT(e.employee_id) 'Num of Employees'
FROM
	locations l
JOIN
	departments d
ON
	l.location_id = d.location_id
JOIN
	employees e
ON
	d.department_id = e.department_id
GROUP BY
	city, state_province
ORDER BY
	'Num of Employees' DESC;


-- Create a query to get the first and last names of all employees and dependents using UNION
SELECT 
	first_name, last_name
FROM
	employees
UNION
SELECT 
	first_name, last_name
FROM
	dependents;

-- Using EXCEPT select employees who make above the average salary for all employees and remove any employees who are managers
SELECT
	first_name, last_name, salary
FROM
	employees
WHERE
	salary > (
	SELECT
		AVG(salary)
	FROM
		employees
	)
EXCEPT
SELECT
	first_name, last_name, salary
FROM
	employees e1
WHERE
	employee_id IN (
	SELECT DISTINCT
		manager_id
	FROM 
		employees
	);

-- Get the job title, the amount of people with that job title, and the average salary for that job title
SELECT 
	j1.job_title, 
	(SELECT	
		COUNT(e2.employee_id)
	FROM
		employees e2
	WHERE 
		e2.job_id = j1.job_id) 'NUM of Employees' , 
	(SELECT	
		AVG(e3.salary)
	FROM
		employees e3
	WHERE 
		e3.job_id = j1.job_id) 'AVG Salary'
FROM 
	jobs j1;
 