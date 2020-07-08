# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

# 返回的长度需要从小到大排列。

# 示例：

# 输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： {3,4,5,6}
# 提示：

# 0 < shorter <= longer
# 0 <= k <= 100000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diving-board-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int):
        if(k == 0):
            return []
        if(shorter == longer):
            return [shorter * k]
        ans = [0]*(k + 1)
        for i in range(k + 1):
            ans[i] = i * longer + (k - i) * shorter
        ans = set(ans)
        ans = list(ans)
        return ans


if __name__ == '__main__':
    solution = Solution()

    print(solution.divingBoard(1, 1, 10))
