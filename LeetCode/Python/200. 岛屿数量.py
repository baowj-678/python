# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量.
# 一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
# 你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3


class Solution:
    def numIslands(self, grid) -> int:
        if(len(grid) == 0):
            return 0
        self.n = len(grid[0])
        self.UF = [0]*(len(grid)*len(grid[0]))
        iosland = []
        for i in range(len(self.UF)):
            self.UF[i] = i
        for i in range(len(self.UF)):
            row = i // self.n
            column = i - row * self.n
            if(grid[row][column] == '0'):
                self.UF[i] = -1
            else:
                if(column > 0 and grid[row][column - 1] == '1'):
                    self.union(i, i - 1)
                if(row > 0 and grid[row - 1][column] == '1'):
                    self.union(i, i - self.n)
        for i in range(len(self.UF)):
            if(self.UF[i] == -1):
                continue
            root = self.root(i)
            if(root not in iosland):
                iosland.append(root)
        return len(iosland)

    def connect(self, a, b):
        while(self.UF[a] != a):
            a = self.UF[a]
        while(self.UF[b] != b):
            b = self.UF[b]
        if(a == b):
            return True
        else:
            return False

    def union(self, a, b):
        while(self.UF[a] != a):
            a = self.UF[a]
        while(self.UF[b] != b):
            b = self.UF[b]
        self.UF[a] = b

    def root(self, i):
        while(self.UF[i] != i):
            i = self.UF[i]
        return i


grid = [["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]]
s = Solution()
print(s.numIslands(grid))
