# 编写一个程序，找出第 n 个丑数。

# 丑数就是只包含质因数 2, 3, 5 的正整数。

# 示例:

# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  

# 1 是丑数。
# n 不超过1690。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        while(len(uglyNums) < n):
            newNum = min(uglyNums[idx2]*2,
                         uglyNums[idx3]*3,
                         uglyNums[idx5]*5)
            if(newNum != uglyNums[-1]):
                uglyNums.append(newNum)
            if(newNum == uglyNums[idx2]*2):
                idx2 += 1
            elif(newNum == uglyNums[idx3]*3):
                idx3 += 1
            elif(newNum == uglyNums[idx5]*5):
                idx5 += 1
        return uglyNums[-1]


s = Solution()
print(s.nthUglyNumber(12))
