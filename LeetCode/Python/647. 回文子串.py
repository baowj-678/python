# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

#  

# 示例 1：

# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：

# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#  

# 提示：

# 输入的字符串长度不会超过 1000 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindromic-substrings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        radius = [0]*len(s)
        i = 0
        R = -1
        C = -1
        while i < len(s):
            if R > i:
                I_mirror = 2 * C - i
                C_mirror = 2 * I_mirror - C
                I_mirror_left = I_mirror - radius[I_mirror] + 1
                if C_mirror < I_mirror_left:
                    radius[i] = radius[I_mirror]
                else:
                    radius[i] = 1
            radius[i] = 1
            while i + radius[i] < len(s) and i - radius[i] >= 0:
                if(s[i + radius[i]] == s[i - radius[i]]):
                    radius[i] += 1
                    R = i + radius[i]
                    C = i
                else:
                    break
            i += 1
        sum_ = 0
        for i in radius[1:-1]:
            i = i - 1
            if(i % 2 == 1):
                sum_ += (i//2 + 1)
            else:
                sum_ += i//2
        return sum_


if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    print(solution.countSubstrings(s))
