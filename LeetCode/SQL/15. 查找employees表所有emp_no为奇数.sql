-- Link: https://www.nowcoder.com/practice/a32669eb1d1740e785f105fa22741d5c?tpId=82&&tqId=29767&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT emp_no, birth_date, first_name, last_name, gender, hire_date
FROM employees
WHERE emp_no % 2 = 1 AND last_name NOT LIKE 'Mary'
ORDER BY hire_date DESC;