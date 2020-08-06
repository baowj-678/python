# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

# 求所能获得硬币的最大数量。

# 说明:

# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 示例:

# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/burst-balloons
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxCoins(self, nums) -> int:
        length = len(nums)
        m = [[0] * length for i in range(length)]
        for i in range(length):
            m[i][i] = nums[i]
        # 长度
        for l in range(1, length, 1):
            # 起点
            for i in range(length - 1):
                end = i + l
                if(end > length - 1):
                    break
                for j in range(i, end + 1, 1):
                    if(j <= i):
                        tmp = m[j + 1][end] + nums[j] * nums[j + 1]
                    elif(j >= end):
                        tmp = m[i][j - 1] + nums[j - 1] * nums[j]
                    else:
                        tmp = m[i][j - 1] + m[j + 1][end] + nums[j - 1] * nums[j] * nums[j + 1]
                    if(tmp > m[i][end]):
                        m[i][end] = tmp
        print(m)
        return m[0][-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1, 5, 8]
    print(solution.maxCoins(nums))

