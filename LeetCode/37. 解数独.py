# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。

# 一个数独。

# 答案被标成红色.

# Note:

# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sudoku-solver
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def solveSudoku(self, board: list) -> None:
        self.rowSet = [set() for i in range(9)]
        self.colSet = [set() for i in range(9)]
        self.blockSet = [[set() for i in range(3)] for j in range(3)]
        self.n = len(board)
        self.coord = []
        x, y = None, None
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == '.':
                    self.coord.append((i, j))
                else:
                    tmp = int(board[i][j])
                    self.rowSet[i].add(tmp)
                    self.colSet[j].add(tmp)
                    self.blockSet[i // 3][j // 3].add(tmp)
                    board[i][j] = tmp

        print(self.blockSet)
        x, y = self.coord[-1]
        self.coord.pop()
        for i in range(1, 10):
            if self.findSolution(board, x, y, i):
                for i in range(9):
                    for j in range(9):
                        board[i][j] = str(board[i][j])
                return None

    def findSolution(self, board, x, y, value):
        if board[x][y] != '.':
            return False
        if value not in self.rowSet[x] and value not in self.colSet[y] and value not in self.blockSet[x // 3][y // 3]:
            board[x][y] = value
            self.rowSet[x].add(value)
            self.colSet[y].add(value)
            self.blockSet[x // 3][y // 3].add(value)
            if len(self.coord) == 0:
                return True
            x_, y_ = self.coord[-1]
            self.coord.pop()
            for i in range(1, 10):
                if self.findSolution(board, x_, y_, i):
                    return True
            self.rowSet[x].remove(value)
            self.colSet[y].remove(value)
            self.blockSet[x // 3][y // 3].remove(value)
            board[x][y] = '.'
            self.coord.append((x_, y_))
            return False


if __name__ == "__main__":
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.solveSudoku(board))
    print(board)
