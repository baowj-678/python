-- Link: https://www.nowcoder.com/practice/4c8b4a10ca5b44189e411107e1d8bec1?tpId=82&&tqId=29761&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT dept_manager.dept_no, salaries.emp_no, salaries.salary
FROM salaries, dept_manager
WHERE dept_manager.emp_no=salaries.emp_no 
AND dept_manager.to_date='9999-01-01'
AND salaries.to_date='9999-01-01'
ORDER BY dept_manager.dept_no ASC;