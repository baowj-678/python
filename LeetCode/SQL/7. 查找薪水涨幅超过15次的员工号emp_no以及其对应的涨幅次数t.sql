-- Link: https://www.nowcoder.com/practice/6d4a4cff1d58495182f536c548fee1ae?tpId=82&&tqId=29759&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/3
-- Code:
SELECT emp_no, COUNT(*)
FROM salaries
GROUP BY emp_no
HAVING COUNT(*) > 15;