-- Link: https://www.nowcoder.com/practice/c63c5b54d86e4c6d880e4834bfd70c3b?tpId=82&&tqId=29755&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/2
-- Code:
SELECT dept_manager.emp_no, salary, from_date, salaries.to_date, dept_no
FROM salaries, dept_manager
WHERE dept_manager.emp_no=salaries.emp_no 
AND dept_manager.to_date='9999-01-01' 
AND salaries.to_date='9999-01-01';