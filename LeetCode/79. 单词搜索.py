# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

#  

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#  

# 提示：

# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def exist(self, board: list, word: str) -> bool:
        if word == "":
            return False
        path = [[0] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.DFS(board, path, word, i, j):
                    return True
        return False

    def DFS(self, board, path, word: str, x, y):
        if len(word) == 0:
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        if path[x][y] == 1 or board[x][y] != word[0]:
            return False
        path[x][y] = 1
        if self.DFS(board, path, word[1:], x - 1, y):
            return True
        if self.DFS(board, path, word[1:], x, y - 1):
            return True
        if self.DFS(board, path, word[1:], x + 1, y):
            return True
        if self.DFS(board, path, word[1:], x, y + 1):
            return True
        path[x][y] = 0
        return False


if __name__ == "__main__":
    solution = Solution()
    board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
            ]
    print(solution.exist(board, 'ABCCED'))
