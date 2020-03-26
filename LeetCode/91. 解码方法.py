# 一条包含字母 A-Z 的消息通过以下方式进行了编码：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 示例 1:

# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:

# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def numDecodings(self, s: str) -> int:
        if(len(s) == 0 or s[0] == '0'):
            return 0
        l_ = [0]*len(s)
        l_[0] = 1
        if(len(s) >= 2):
            if(int(s[1]) == 0):
                if(int(s[0:2]) <= 26):
                    l_[1] = 1
                else:
                    l_[1] = 0
                    return 0
            else:
                if(int(s[0:2]) <= 26):
                    l_[1] = 2
                else:
                    l_[1] = 1
        for i in range(2, len(s), 1):
            if(s[i - 1] == '0'):
                if(s[i] != '0'):
                    l_[i] = l_[i - 1]
                else:
                    return 0
            else:
                if(s[i] == '0'):
                    if(int(s[i - 1:i + 1]) <= 26):
                        l_[i] = l_[i - 2]
                    else:
                        l_[i] = 0
                        return 0
                else:
                    if(int(s[i-1: i+1]) <= 26):
                        l_[i] = l_[i - 1] + l_[i - 2]
                    else:
                        l_[i] = l_[i - 1]
        return l_[len(s) - 1]


s = '101'
so = Solution()
print(so.numDecodings(s))
