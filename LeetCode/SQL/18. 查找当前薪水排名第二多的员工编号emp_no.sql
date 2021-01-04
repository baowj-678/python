-- Link: https://www.nowcoder.com/practice/c1472daba75d4635b7f8540b837cc719?tpId=82&&tqId=29770&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT employees.emp_no, salary, last_name, first_name 
FROM employees INNER JOIN salaries
ON employees.emp_no=salaries.emp_no 
WHERE to_date = '9999-01-01' AND salary = 
(SELECT MAX(salary) FROM salaries 
WHERE salary <> (SELECT MAX(salary) FROM salaries WHERE to_date = '9999-01-01') 
AND to_date = '9999-01-01');