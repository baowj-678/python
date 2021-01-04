-- Link: https://www.nowcoder.com/practice/8d2c290cc4e24403b98ca82ce45d04db?tpId=82&&tqId=29769&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT emp_no, salary
FROM salaries
WHERE to_date='9999-01-01'
ORDER BY salary DESC LIMIT 1, 1;