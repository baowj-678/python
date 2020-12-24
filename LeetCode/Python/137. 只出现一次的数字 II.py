# 137. 只出现一次的数字 II
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,3,2]
# 输出: 3
# 示例 2:

# 输入: [0,1,0,1,0,1,99]
# 输出: 99


class Solution:
    def singleNumber(self, nums) -> int:
        repeat = [0]*40
        position = [0]*40
        for i in range(40):
            position[i] = 1 << i
        for i in range(len(nums)):
            for j in range(40):
                repeat[j] += (nums[i] & position[j]) >> j
        sum = 0
        for j in range(40):
            repeat[j] -= 3*(repeat[j]//3)
            if(repeat[j] > 0):
                sum |= (1 << j)
        if(repeat[39] != 0):
            sum -= 2**40
            pass
        print(repeat)
        return int(sum)


def main():
    nums = [43, 16, 45,
            89, 45, -2147483648,
            45, 2147483646, -2147483647,
            -2147483648, 43, 2147483647,
            -2147483646, -2147483648, 89,
            -2147483646, 89, -2147483646,
            -2147483647, 2147483646, -2147483647,
            16, 16, 2147483646,
            43]
    s = Solution()
    print(s.singleNumber(nums))


main()
