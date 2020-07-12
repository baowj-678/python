# 你将得到一个字符串数组 A。

# 每次移动都可以交换 S 的任意两个偶数下标的字符或任意两个奇数下标的字符。

# 如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是 特殊等价 的。

# 例如，S = "zzxy" 和 T = "xyzz" 是一对特殊等价字符串，因为可以先交换 S[0] 和 S[2]，然后交换 S[1] 和 S[3]
# 使得 "zzxy" -> "xzzy" -> "xyzz" 。

# 现在规定，A 的 一组特殊等价字符串 就是 A 的一个同时满足下述条件的非空子集：
# 该组中的每一对字符串都是 特殊等价的
# 该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中
# 那么这个字符串就不会与该组内任何字符串特殊等价）
# 返回 A 中特殊等价字符串组的数量。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/groups-of-special-equivalent-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        s = set()
        for sent in A:
            sub = ''.join(sorted(sent[::2]) + sorted(sent[1::2]))
            s.add(sub)
        return len(s)


if __name__ == '__main__':
    solution = Solution()
    A = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    print(solution.numSpecialEquivGroups(A))
