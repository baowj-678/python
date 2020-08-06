# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

# 示例 1:

# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]]
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 示例 2:

# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]]
# 解释: 可拼接成的回文串为 ["battab","tabbat"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def palindromePairs(self, words):

        def isPalindrom(s):
            i, j = 0, len(s) - 1
            while(i < j):
                if(s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True
        rev = {}
        pairs = set()
        for index, word in enumerate(words):
            rev[word[::-1]] = index
        for index, word in enumerate(words):
            if(word == ''):
                for i, word in enumerate(words):
                    if(isPalindrom(word) and i != index):
                        pairs.add('{},{}'.format(index, i))
            for i in range(len(word)):
                left = word[:i]
                right = word[i:]
                if(isPalindrom(left)):
                    if(right in rev and rev[right] != index):
                        pairs.add('{},{}'.format(rev[right], index))
                if(isPalindrom(right)):
                    if(left in rev and rev[left] != index):
                        pairs.add('{},{}'.format(index, rev[left]))
        ans = []
        for s in pairs:
            s = s.split(',')
            ans.append([int(s[0]), int(s[1])])
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["bat", "tab", "cat"]
    print(solution.palindromePairs(words))
