# 167. 两数之和 II - 输入有序数组
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:

# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


class Solution:
    # bad method
    def twoSum(self, numbers, target: int):
        ans = [0] * 2
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers), 1):
                if(numbers[i] + numbers[j] == target):
                    ans[0] = i + 1
                    ans[1] = j + 1
                    return ans
        return

    # good method
    def twoSumBetter(self, numbers, target: int):
        ans = [0] * 2
        i = 0
        j = len(numbers) - 1
        while(i < j):
            if(numbers[i] + numbers[j] > target):
                j -= 1
            elif(numbers[i] + numbers[j] < target):
                i += 1
            else:
                ans[0] = i + 1
                ans[1] = j + 1
                break
        return ans


def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSumBetter(nums, target))


main()
