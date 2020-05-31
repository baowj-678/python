# 84. 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
# 示例:

# 输入: [2,1,5,6,2,3]
# 输出: 10


class Solution:
    def largestRectangleArea(self, heights) -> int:
        square = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            while(len(square) > 0 and heights[square[-1]] > heights[i]):
                height = heights[square[-1]]
                square.pop()
                if(len(square) > 0):
                    left = square[-1] + 1
                else:
                    left = 0
                right = i - 1
                maxArea = max(maxArea, (right - left + 1) * height)
            square.append(i)
        return maxArea
        # left, right = 0, len(heights) - 1
        # maxHeight, maxLeftHeight, maxRightHeight = 0, 0, 0
        # maxSquare = 0
        # while(left <= right):
        #     if(heights[left] > heights[right]):
        #         square = heights[right] * (right - left + 1)
        #         if(square > maxSquare):
        #             maxSquare = square
        #             maxRightHeight = heights[right]
        #             maxLeftHeight = heights[left]
        #         right -= 1
        #     else:
        #         square = heights[left] * (right - left + 1)
        #         if(square > maxSquare):
        #             maxSquare = square
        #             maxLeftHeight = heights[left]
        #             maxRightHeight = heights[right]
        #         left += 1
        # return maxSquare


if __name__ == '__main__':
    nums = [1, 8]
    s = Solution()
    print(s.largestRectangleArea(nums))
