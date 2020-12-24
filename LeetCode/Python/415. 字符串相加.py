# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

# 注意：

# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        num = ''
        tmp = 0
        i = 0
        n = max(len(num1), len(num2))
        for i in range(n):
            a, b = 0, 0
            if(i < len(num1)):
                a = int(num1[i])
            if(i < len(num2)):
                b = int(num2[i])
            tmp += (a + b)
            num += str(tmp % 10)
            tmp //= 10
        if(tmp > 0):
            num += str(tmp)
        return num[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addStrings('89123', '9'))
