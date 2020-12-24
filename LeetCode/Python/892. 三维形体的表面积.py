# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

# 请你返回最终形体的表面积。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def surfaceArea(self, grid) -> int:
        S = 0
        x, y = len(grid), len(grid[0])
        for i in range(x):
            for j in range(y):
                if i > 0:
                    if grid[i - 1][j] < grid[i][j]:
                        S += grid[i][j] - grid[i - 1][j]
                else:
                    S += grid[i][j]

                if j > 0:
                    if grid[i][j - 1] < grid[i][j]:
                        S += grid[i][j] - grid[i][j - 1]
                else:
                    S += grid[i][j]

                if i < x - 1:
                    if grid[i + 1][j] < grid[i][j]:
                        S += grid[i][j] - grid[i + 1][j]
                else:
                    S += grid[i][j]

                if j < y - 1:
                    if grid[i][j + 1] < grid[i][j]:
                        S += grid[i][j] - grid[i][j + 1]
                else:
                    S += grid[i][j]

                if grid[i][j] != 0:
                    S += 2
        return S


if __name__ == "__main__":
    solution = Solution()
    grid = [[]]
    print(solution.surfaceArea(grid))
