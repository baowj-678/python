-- Link: https://www.nowcoder.com/practice/ec1ca44c62c14ceb990c3c40def1ec6c?tpId=82&&tqId=29754&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/2
-- Code:
SELECT *
FROM employees
ORDER BY `employees`.`hire_date` DESC
LIMIT 2, 1