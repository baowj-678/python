-- Link: https://www.nowcoder.com/practice/72ca694734294dc78f513e147da7821e?tpId=82&&tqId=29765&rp=1&ru=/ta/sql&qru=/ta/sql/question-ranking
-- Date: 2021/1/4
-- Code:
SELECT title, COUNT(*)
FROM titles
GROUP BY title;