-- Link: https://www.nowcoder.com/practice/5a7975fabe1146329cee4f670c27ad55?tpId=82&&tqId=29771&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT employees.last_name, employees.first_name, departments.dept_name
FROM (employees LEFT JOIN dept_emp ON employees.emp_no=dept_emp.emp_no) 
LEFT JOIN departments ON dept_emp.dept_no=departments.dept_no;
