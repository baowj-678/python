# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def permuteUnique(self, nums):
        if(len(nums) == 0):
            return [[]]
        nums = sorted(nums)
        return Solution.DFS(nums)

    def DFS(nums):
        if(len(nums) == 1):
            return [[nums[0]]]
        ans = []
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            else:
                numCopy = nums.copy()
                del(numCopy[i])
                numCopy = Solution.DFS(numCopy)
                for subNumCopy in numCopy:
                    ans.append([nums[i]] + subNumCopy)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = []
    print(s.permuteUnique(nums))
