-- Link: https://www.nowcoder.com/practice/c8652e9e5a354b879e2a244200f1eaae?tpId=82&&tqId=29768&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT title, AVG(salary)
FROM titles, salaries
WHERE titles.emp_no=salaries.emp_no AND titles.to_date='9999-01-01' AND salaries.to_date='9999-01-01'
GROUP BY title;