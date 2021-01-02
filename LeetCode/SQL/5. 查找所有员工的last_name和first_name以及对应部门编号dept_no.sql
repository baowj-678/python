-- Link: https://www.nowcoder.com/practice/dbfafafb2ee2482aa390645abd4463bf?tpId=82&&tqId=29757&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT last_name, first_name, dept_no
FROM employees LEFT JOIN dept_emp
ON employees.emp_no=dept_emp.emp_no;