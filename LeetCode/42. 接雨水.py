# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#  感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


class Solution:
    def trap(self, height) -> int:
        left, pleft = 0, 0
        right, pright = len(height) - 1, len(height) - 1
        water = 0
        heightest = 0
        isLeft, isRight = True, True
        for h in height:
            if(h > heightest):
                heightest = h
        while(pleft <= pright):
            if(isLeft is False and isRight is False):
                water += (heightest - height[pleft])
                pleft += 1
            else:
                delta = height[left] - height[pleft]
                if(isLeft):
                    if(delta >= 0):
                        water += delta
                    else:
                        left = pleft
                    if(height[pleft] == heightest):
                        isLeft = False
                    pleft += 1
                delta = height[right] - height[pright]
                if(isRight):
                    if(delta >= 0):
                        water += delta
                    else:
                        right = pright
                    if(height[pright] == heightest):
                        isRight = False
                    pright -= 1
        return water


if __name__ == '__main__':
    s = Solution()
    height = [1]
    print(s.trap(height))
