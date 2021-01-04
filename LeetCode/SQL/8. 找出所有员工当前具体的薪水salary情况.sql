-- Link: https://www.nowcoder.com/practice/ae51e6d057c94f6d891735a48d1c2397?tpId=82&&tqId=29760&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT DISTINCT(salary)
FROM salaries
WHERE to_date='9999-01-01'
ORDER BY salary DESC;