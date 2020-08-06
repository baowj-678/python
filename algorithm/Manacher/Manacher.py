"""
@Description: Manacher算法的实现
@Author: Bao Wenjie
@Date: 2020/8/6
@Email: bwj_678@qq.com
"""


def Manacher(s: str):
    """
    @description: Manacher算法
    @param s: 字符串
    """
    # 字符串预处理
    s = '#' + '#'.join(s) + '#'
    # 变量初始化
    radius = [0] * len(s)
    R = -1
    C = -1
    for i in range(len(s)):
        # 下一个移动位置在R之内
        if(R > i):
            radius[i] = min(radius[2 * C - i], R - i + 1)
        else:
            radius[i] = 1
        while(i + radius[i] < len(s) and i - radius[i] > -1):
            if(s[i - radius[i]] == s[i + radius[i]]):
                radius[i] += 1
            else:
                break
        if(i + radius[i] > R):
            R = i + radius[i] - 1
            C = i
    return max(radius) - 1


if __name__ == '__main__':
    s = 'jffwuefh'
    print(Manacher(s))
