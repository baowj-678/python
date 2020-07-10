# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，
# 你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:

# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 0:
            return 0
        sells = [0] * n
        cools = [0] * n
        buys = [0] * n
        buys[0] = -prices[0]
        for i in range(1, n):
            sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
            buys[i] = max(buys[i - 1], cools[i - 1] - prices[i])
            cools[i] = max(buys[i - 1], sells[i - 1], cools[i - 1])
        n -= 1
        return max(sells[n], cools[n], buys[n])


if __name__ == "__main__":
    solution = Solution()
    num = [1, 2, 3, 0, 2]
    print(solution.maxProfit(num))
