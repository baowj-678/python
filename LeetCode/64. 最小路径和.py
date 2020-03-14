class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        if(m == 0):
            return 0
        n = len(grid[0])
        s = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            s[i][n] = float('inf')
        for i in range(n + 1):
            s[m][i] = float('inf')
        s[m][n - 1] = s[m - 1][n] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                s[i][j] = min(s[i + 1][j], s[i][j + 1]) + grid[i][j]
        print(s)
        return s[0][0]


s = Solution()
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print(s.minPathSum(grid))
