# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

#  

# 示例 1:

# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 示例 2:

# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#  

# 提示：

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/divide-two-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend ^ divisor) < 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if((dividend >> i) >= divisor):
                result += 1 << i
                dividend -= divisor << i
        if(is_negative):
            return -result
        else:
            if(result > 2147483647):
                return 2147483647
            return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(-2147483648, -1))
