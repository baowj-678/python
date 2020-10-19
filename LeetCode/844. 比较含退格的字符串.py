# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

# 注意：如果对空文本输入退格字符，文本继续为空。

#  

# 示例 1：

# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
# 示例 2：

# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
# 示例 3：

# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
# 示例 4：

# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
#  

# 提示：

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S 和 T 只含有小写字母以及字符 '#'。
#  

# 进阶：

# 你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/backspace-string-compare
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        s_p = 0
        t_p = 0
        for i in range(len(S)):
            if S[i] == '#':
                if s_p > 0:
                    s_p -= 1
            else:
                S[s_p] = S[i]
                s_p += 1
        for i in range(len(T)):
            if T[i] == '#':
                if t_p > 0:
                    t_p -= 1
            else:
                T[t_p] = T[i]
                t_p += 1
        if s_p != t_p:
            return False
        else:
            for i in range(s_p):
                if S[i] != T[i]:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))
