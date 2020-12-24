# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combinations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def combine(self, n: int, k: int):
        if k == 0:
            return []
        self.ans = []
        self.combine_two(n + 1, k, 1, [])
        return self.ans

    def combine_two(self, n, k: int, m: int, combined_nums: list):
        if k == 1:
            if m < n:
                for i in range(m, n):
                    tmp = combined_nums + [i]
                    self.ans.append(tmp)
        else:
            for i in range(m, n):
                tmp = combined_nums + [i]
                self.combine_two(n, k - 1, i + 1, tmp)


if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(5, 2))
