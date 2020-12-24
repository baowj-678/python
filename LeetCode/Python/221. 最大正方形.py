# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4


class Solution:
    def maximalSquare(self, matrix) -> int:
        maxSize = 0
        x = len(matrix)
        if(x == 0):
            return 0
        y = len(matrix[0])
        for k in range(y):
            if(matrix[0][k] == '1'):
                matrix[0][k] = 1
                maxSize = 1
            else:
                matrix[0][k] = 0
        for i in range(1, x):
            if(matrix[i][0] == '1'):
                matrix[i][0] = 1
                if(maxSize == 0):
                    maxSize = 1
            else:
                matrix[i][0] = 0
            for j in range(1, y):
                if(matrix[i][j] == '1'):
                    if(matrix[i - 1][j - 1] > 0 and
                       matrix[i - 1][j] > 0 and
                       matrix[i][j - 1] > 0):
                        matrix[i][j] = matrix[i - 1][j - 1] + 1
                    else:
                        matrix[i][j] = 0
                    if(matrix[i][j] > maxSize):
                            maxSize = matrix[i][j]
                else:
                    matrix[i][j] = 0
        print(matrix)
        return maxSize**2


matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
s = Solution()
print(s.maximalSquare(matrix))
