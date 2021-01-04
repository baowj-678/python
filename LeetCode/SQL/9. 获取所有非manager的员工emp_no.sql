-- Link: https://www.nowcoder.com/practice/32c53d06443346f4a2f2ca733c19660c?tpId=82&&tqId=29762&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT emp_no
FROM employees
WHERE emp_no NOT IN(
SELECT emp_no
FROM dept_manager);