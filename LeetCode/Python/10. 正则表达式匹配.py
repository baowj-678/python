# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:

# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:

# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:

# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import numpy as np


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if(len(p) == 0 and len(s) == 0):
            return True
        if(len(p) == 0):
            return False

        keys = []
        i = 0
        while(i < len(p)):
            if(p[i].isalpha() or p[i] == '.'):
                if(i + 1 < len(p) and p[i + 1] == '*'):
                    keys.append(p[i] + p[i + 1])
                    i += 2
                else:
                    keys.append(p[i])
                    i += 1
        if(len(s) == 0):
            for key in keys:
                if(len(key) == 1):
                    return False
            return True

        graph = np.zeros([len(keys), len(s)])
        isFirst = True
        for i, key in enumerate(keys):
            for j in range(0, len(s)):
                if(len(key) == 1):
                    # match ok
                    if((key.isalpha() and key == s[j]) or key == '.'):
                        if(j - 1 >= 0):
                            if(i - 1 >= 0 and graph[i - 1, j - 1] == 1):
                                graph[i, j] = 1
                        elif(isFirst and j == 0):
                            graph[i, j] = 1
                    isFirst = False
                else:
                    if(i - 1 >= 0 and graph[i - 1, j] == 1):
                        graph[i, j] = 1
                    if((key[0].isalpha() and key[0] == s[j]) or key[0] == '.'):
                        if(j - 1 >= 0):
                            if(graph[i - 1, j - 1] == 1 or
                               graph[i, j - 1] == 1):
                                graph[i, j] = 1
                        elif(isFirst and j == 0):
                            graph[i, j] = 1
        print(graph)
        if(graph[len(keys) - 1, len(s) - 1] == 1):
            return True
        else:
            return False

    # match p and the part of s
    def isMatchPart(self, s: str, p: str) -> bool:
        if(len(s) == 0 and len(p) == 0):
            return False

        nowPointS, nowPointP = 0, 0
        while(nowPointP < len(p)):
            # is alphabet
            if(p[nowPointP].isalpha()):
                # alphabet*n
                if(nowPointP + 1 < len(p) and p[nowPointP + 1] == '*'):
                    nowPointP += 2
                # just alphabet
                else:
                    isFind = False
                    while(nowPointS < len(s)):
                        if(s[nowPointS] == p[nowPointP]):
                            isFind = True
                            nowPointS += 1
                            break
                        else:
                            nowPointS += 1
                    if(isFind is False):
                        return False
                    nowPointP += 1
            # is .
            elif(p[nowPointP] == '.'):
                # .*n
                if(nowPointP + 1 < len(p) and p[nowPointP + 1] == '*'):
                    pass
                # .
                else:
                    nowPointS += 1
                    if(nowPointS > len(s)):
                        return False
                nowPointP += 1
        return True


if __name__ == '__main__':
    so = Solution()
    s = ""
    p = "c*a*"
    print(so.isMatch(s, p))
