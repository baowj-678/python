-- Link: https://www.nowcoder.com/practice/23142e7a23e4480781a3b978b5e0f33a?tpId=82&&tqId=29758&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT employees.emp_no, salaries.salary
FROM employees, salaries
WHERE employees.emp_no=salaries.emp_no 
AND DATE(employees.hire_date) BETWEEN salaries.from_date AND salaries.to_date
ORDER BY employees.emp_no DESC;