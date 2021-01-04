-- Link: https://www.nowcoder.com/practice/c59b452f420c47f48d9c86d69efdff20?tpId=82&&tqId=29766&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT title, COUNT(DISTINCT emp_no)
FROM titles
GROUP BY title;