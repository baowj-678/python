# 给定一个整数矩阵，找出最长递增路径的长度。

# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

# 示例 1:

# 输入: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 示例 2:

# 输入: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if(matrix == [] or matrix == [[]]):
            return 0
        pathLength = [[-1] * len(matrix[0]) for i in range(len(matrix))]
        height = len(matrix) - 1
        width = len(matrix[0]) - 1

        def DFS(matrix, pathLength, x, y):
            if(pathLength[x][y] != -1):
                return pathLength[x][y]
            else:
                if(x < height and matrix[x][y] > matrix[x + 1][y]):
                    above = 1 + DFS(matrix, pathLength, x + 1, y)
                else:
                    above = 1

                if(x > 0 and matrix[x][y] > matrix[x - 1][y]):
                    under = 1 + DFS(matrix, pathLength, x - 1, y)
                else:
                    under = 1

                if(y > 0 and matrix[x][y] > matrix[x][y - 1]):
                    left = 1 + DFS(matrix, pathLength, x, y - 1)
                else:
                    left = 1

                if(y < width and matrix[x][y] > matrix[x][y + 1]):
                    right = 1 + DFS(matrix, pathLength, x, y + 1)
                else:
                    right = 1
                tmp1 = max(above, under)
                tmp2 = max(left, right)
                pathLength[x][y] = max(tmp1, tmp2)
                return pathLength[x][y]

        max_ = 0
        for x in range(height + 1):
            for y in range(width + 1):
                tmp = DFS(matrix, pathLength, x, y)
                if(tmp > max_):
                    max_ = tmp
        print(pathLength)
        return max_


if __name__ == '__main__':
    solution = Solution()
    nums = [[9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]]
    print(solution.longestIncreasingPath(nums))
