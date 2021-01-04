-- Link: https://www.nowcoder.com/practice/4a052e3e1df5435880d4353eb18a91c6?tpId=82&&tqId=29764&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT d1.dept_no, d1.emp_no, s1.salary
FROM salaries s1, dept_emp d1
WHERE d1.emp_no=s1.emp_no AND d1.to_date='9999-01-01' AND s1.to_date='9999-01-01' 
AND s1.salary>=ALL(
SELECT s2.salary
FROM salaries s2, dept_emp d2
WHERE d2.emp_no=s2.emp_no AND d2.to_date='9999-01-01' AND s2.to_date='9999-01-01'
AND d2.dept_no=d1.dept_no)
ORDER BY d1.dept_no ASC;