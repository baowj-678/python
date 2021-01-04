-- Link: https://www.nowcoder.com/practice/e50d92b8673a440ebdf3a517b5b37d62?tpId=82&&tqId=29763&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT dept_emp.emp_no, dept_manager.emp_no
FROM dept_emp, dept_manager
WHERE dept_emp.dept_no=dept_manager.dept_no
AND dept_emp.emp_no <> dept_manager.emp_no
AND dept_manager.to_date='9999-01-01';