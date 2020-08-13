# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：

# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/multiply-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = ''
        for i in range(len(num2)):
            tmp = self.mm(num1, num2[-i - 1])
            if tmp[0] == '0':
                tmp = '0'
            else:
                tmp = tmp + '0'*i
            ans = self.add(tmp, ans)
        return ans

    def mm(self, num1, num2):
        ans = ''
        n = len(num1)
        num2 = int(num2)
        if(num2 == 0):
            return '0'
        move = 0
        for i in range(-1, -(n + 1), -1):
            tmp = int(num1[i]) * num2 + move
            ans = str(tmp % 10) + ans
            move = tmp // 10
        if move > 0:
            ans = str(move) + ans
        return ans

    def add(self, num1, num2):
        ans = ''
        n = max(len(num1), len(num2))
        move = 0
        for i in range(-1, -(n + 1), -1):
            n1, n2 = 0, 0
            if(i > -len(num1) - 1):
                n1 = int(num1[i])
            if(i > -len(num2) - 1):
                n2 = int(num2[i])
            tmp = n1 + n2 + move
            ans = str(tmp % 10) + ans
            move = tmp // 10
        if move > 0:
            ans = str(move) + ans
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply('13528', '0'))
