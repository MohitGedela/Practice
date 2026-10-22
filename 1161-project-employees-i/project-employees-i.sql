SELECT project_id, ROUND(SUM(experience_years)/COUNT(experience_years), 2) as average_years
FROM Project LEFT OUTER JOIN Employee on Project.employee_id = Employee.employee_id
GROUP BY project_id