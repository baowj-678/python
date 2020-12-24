# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）。

#  

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


class Solution:
    def maxProduct(self, nums) -> int:
        mx = nums[0]
        positive = -99999
        negative = 0
        temp = 0
        for i in range(len(nums)):
            if(nums[i] > 0):
                if(positive == -99999 or positive == 0):
                    positive = nums[i]
                else:
                    positive *= nums[i]
                negative *= nums[i]
            elif(nums[i] < 0):
                if(negative == 0):
                    if(positive == -99999 or positive == 0):
                        negative = nums[i]
                    else:
                        negative = positive * nums[i]
                        positive = 0
                else:
                    if(positive == -99999 or positive == 0):
                        positive = negative * nums[i]
                        negative = nums[i]
                    else:
                        temp = negative
                        negative = positive * nums[i]
                        positive = temp * nums[i]
            else:
                positive = 0
                negative = 0
            if(positive > mx):
                mx = positive
        return mx


s = Solution()
num = [-2]
print(s.maxProduct(num))
