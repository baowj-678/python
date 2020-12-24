class Solution:
    def maxProfit(self, prices):
        if(len(prices) == 0):
            return 0
        min = prices[0]
        max_profit = 0
        temp = 0
        for i in range(len(prices)):
            temp = prices[i] - min
            if(temp > max_profit):
                max_profit = temp
            if(prices[i] < min):
                min = prices[i]
        return max_profit


def main():
    nums = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(nums))


main()
