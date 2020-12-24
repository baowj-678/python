# 给定一个包含 n 个整数的数组 nums 和一个目标值 target
# 判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
# 找出所有满足条件且不重复的四元组。

# 注意：

# 答案中不可以包含重复的四元组。

# 示例：

# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def fourSum(self, nums, target: int):
        ans = []
        nums = sorted(nums)
        i, j, p, q = 0, 0, 0, 0
        lastI = None
        while(i < len(nums) - 3):
            if(lastI == nums[i]):
                i += 1
                continue
            lastI = nums[i]
            j = i + 1
            lastJ = None
            while(j < len(nums) - 2):
                if(lastJ == nums[j]):
                    j += 1
                    continue
                lastJ = nums[j]
                sumIJ = nums[i] + nums[j]
                p, q = j + 1, len(nums) - 1
                lastP = None
                while(p < q):
                    sumALL = nums[p] + nums[q] + sumIJ
                    if(sumALL == target):
                        if(lastP != nums[p]):
                            ans.append([nums[i], nums[j], nums[p], nums[q]])
                        lastP = nums[p]
                        p += 1
                        q -= 1
                    elif(sumALL < target):
                        p += 1
                    elif(sumALL > target):
                        q -= 1
                j += 1
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(s.fourSum(nums, target))
