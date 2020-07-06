# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def searchRange(self, nums, target: int):
        ans = [0, 0]
        ans[0] = self.searchLow(nums, target)
        ans[1] = self.searchHigh(nums, target)
        return ans

    def searchLow(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            half = (left + right) // 2
            if(nums[half] == target):
                if(half > 0):
                    if(nums[half - 1] == target):
                        right = half - 1
                    else:
                        return half
                else:
                    return half
            elif(nums[half] > target):
                right = half - 1
            else:
                left = half + 1
        return -1

    def searchHigh(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            half = (left + right) // 2
            if(nums[half] == target):
                if(half < len(nums) - 1):
                    if(nums[half + 1] == target):
                        left = half + 1
                    else:
                        return half
                else:
                    return half
            elif(nums[half] > target):
                right = half - 1
            else:
                left = half + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 5]
    target = 5
    print(solution.searchRange(nums, target))
