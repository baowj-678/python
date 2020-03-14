class Solution:
    def rob(self, nums) -> int:
        if(len(nums) == 0):
            return 0
        elif(len(nums) == 1):
            return nums[0]
        n_minus_2 = nums[0]
        n_minus_1 = max(nums[0], nums[1])
        temp = 0
        for i in range(2, len(nums)):
            if(n_minus_1 == n_minus_2):
                n_minus_1 += nums[i]
            else:
                temp = n_minus_1
                n_minus_1 = n_minus_2 + nums[i]
                n_minus_2 = temp
                n_minus_1 = max(n_minus_1, n_minus_2)
        return max(n_minus_1, n_minus_2)


def main():
    nums = [1, 3, 1, 3, 100]
    s = Solution()
    print(s.rob(nums))


main()
