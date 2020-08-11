# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

# 示例:

# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：

# X X X X
# X X X X
# X X X X
# X O X X
# 解释:

# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surrounded-regions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if(board == [] or board == [[]]):
            return
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            self.checkZeros(i, 0, board)
            self.checkZeros(i, self.m - 1, board)
        for i in range(self.m):
            self.checkZeros(0, i, board)
            self.checkZeros(self.n - 1, i, board)
        for i in range(self.n):
            for j in range(self.m):
                if(board[i][j] == '*'):
                    board[i][j] = 'O'
                elif(board[i][j] == 'O'):
                    board[i][j] = 'X'

    def checkZeros(self, i, j, board):
        if(board[i][j] == 'O'):
            board[i][j] = '*'
        else:
            return
        if(i > 0):
            self.checkZeros(i - 1, j, board)
        if(i < self.n - 1):
            self.checkZeros(i + 1, j, board)
        if(j > 0):
            self.checkZeros(i, j - 1, board)
        if(j < self.m - 1):
            self.checkZeros(i, j + 1, board)


if __name__ == '__main__':
    solution = Solution()
    board = [['X']]
    print(solution.solve(board))
    print(board)
