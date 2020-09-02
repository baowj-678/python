# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return False
        else:
            if s[0] == '-' or s[0] == '+':
                s = s[1:]
            if s.isdigit():
                return True
            i = 0
            while (i < len(s) and s[i] != 'e' and s[i] != 'E'):
                i += 1
            if i < len(s) and (s[i] == 'e' or s[i] == 'E'):
                if (s[0:i].isdigit() is False and self.isPoint(s[0:i]) is False) or i == len(s) - 1:
                    return False
                if s[i + 1] == '-' or s[i + 1] == '+':
                    i += 1
                if s[i + 1:].isdigit():
                    return True
                return False
            else:
                return self.isPoint(s)

    def isPoint(self, s):
        if len(s) == 1:
            return False
        i = 0
        while i < len(s) and s[i] != '.':
            i += 1
        if i == len(s):
            return False
        if s[0:i].isdigit() is False and i > 0:
            return False
        if i == len(s) - 1 or s[i + 1:].isdigit():
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    s = '01232'
    print(solution.isNumber(s))
