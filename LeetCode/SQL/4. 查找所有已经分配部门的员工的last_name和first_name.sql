-- Link: https://www.nowcoder.com/practice/6d35b1cd593545ab985a68cd86f28671?tpId=82&&tqId=29756&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT last_name, first_name, dept_no
FROM dept_emp LEFT JOIN employees
ON dept_emp.emp_no=employees.emp_no;