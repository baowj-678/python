# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s == ''):
            return True
        left = 0
        right = len(s) - 1
        left_chara = s[left]
        right_chara = s[right]
        while(left < right):
            if(not (left_chara.isalpha() or left_chara.isdigit())):
                left += 1
                left_chara = s[left]
                continue
            if(not (right_chara.isalpha() or right_chara.isdigit())):
                right -= 1
                right_chara = s[right]
                continue
            if(right_chara.lower() == left_chara.lower()):
                left += 1
                right -= 1
                left_chara = s[left]
                right_chara = s[right]
            else:
                return False
        return True


def main():
    st = "0P"
    s = Solution()
    print(s.isPalindrome(st))


main()
