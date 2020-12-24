# 给定一副牌，每张牌上都写着一个整数。

# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。

#  

# 示例 1：

# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 示例 2：

# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 示例 3：

# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 示例 4：

# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 示例 5：

# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]

# 提示：

# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        def gcd(x, y):
            if(x == 0 or y == 0):
                return None
            else:
                big = max(x, y)
                small = min(x, y)
                while(big > small and small != 0):
                    tmp = small
                    small = big % small
                    big = tmp
                return big
        # 统计出现次数
        num2sum = [0]*10000
        for i in range(len(deck)):
            num2sum[deck[i]] += 1
        g = -1
        for num in num2sum:
            if(num > 0):
                if(g == -1):
                    g = num
                else:
                    g = gcd(g, num)
        if(g >= 2):
            return True
        else:
            return False


s = Solution()
num = []
print(s.hasGroupsSizeX(num))
