class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(n + 1):
            s[m][i] = 0
        for i in range(m + 1):
            s[i][n] = 0
        s[m - 1][n] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                s[j][i] = s[j + 1][i] + s[j][i + 1]
        print(s)
        return s[0][0]


def main():
    s = Solution()
    print(s.uniquePaths(7, 3))
    pass


main()
