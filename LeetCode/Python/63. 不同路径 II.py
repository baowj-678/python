class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        if(m == 0):
            return 0
        n = len(obstacleGrid[0])
        s = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(n + 1):
            s[m][i] = 0
        for i in range(m + 1):
            s[i][n] = 0
        s[m][n - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if(obstacleGrid[j][i] == 1):
                    s[j][i] = 0
                else:
                    s[j][i] = s[j + 1][i] + s[j][i + 1]
        return s[0][0]


s = Solution()
o = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
print(s.uniquePathsWithObstacles(o))
