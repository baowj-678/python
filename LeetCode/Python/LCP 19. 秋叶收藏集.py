# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

# 示例 1：

# 输入：leaves = "rrryyyrryyyrr"

# 输出：2

# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

# 示例 2：

# 输入：leaves = "ryr"

# 输出：0

# 解释：已符合要求，不需要额外操作

# 提示：

# 3 <= leaves.length <= 10^5
# leaves 中只包含字符 'r' 和字符 'y'

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/UlBDOe
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import numpy as np


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        dp = np.zeros((len(leaves), 3))
        for i, leave in enumerate(leaves):
            if leave == 'r':
                dp[i, 0] = dp[i - 1, 0]
                if i == 1:
                    dp[i, 1] = dp[i - 1, 0] + 1
                else:
                    dp[i, 1] = min(dp[i - 1, 0] + 1, dp[i - 1, 1] + 1)
                if i == 2:
                    dp[i, 2] = dp[i - 1, 1]
                else:
                    dp[i, 2] = min(dp[i - 1, 1], dp[i - 1, 2])

            elif leave == 'y':
                dp[i, 0] = dp[i - 1, 0] + 1
                if i == 1:
                    dp[i, 1] = dp[i - 1, 0]
                else:
                    dp[i, 1] = min(dp[i - 1, 0], dp[i - 1, 1])

                if i == 2:
                    dp[i, 2] = dp[i - 1, 1] + 1
                else:
                    dp[i, 2] = min(dp[i - 1, 1] + 1, dp[i - 1, 2] + 1)
        print(dp)
        return int(dp[-1, 2])


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOperations("yryyrry"))
