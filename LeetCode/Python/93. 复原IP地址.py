# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

#  

# 示例:

# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/restore-ip-addresses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def restoreIpAddresses(self, s: str):
        self.ans = []
        self.getIP(s, [])
        return self.ans

    def getIP(self, s, a: list):
        if(len(a) >= 4 and len(s) > 0):
            return
        elif(len(a) == 4 and len(s) == 0):
            self.ans.append('.'.join([str(a_) for a_ in a]))
        for i in range(1, len(s) + 1):
            if(s[0] == '0' and i > 1):
                break
            num = int(s[:i])
            if 0 <= num <= 255:
                a.append(num)
                self.getIP(s[i:], a)
                a.pop()
            else:
                break


if __name__ == '__main__':
    solution = Solution()
    s = "0000"
    print(solution.restoreIpAddresses(s))
