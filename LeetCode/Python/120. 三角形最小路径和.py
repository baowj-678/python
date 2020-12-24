# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def minimumTotal(self, triangle) -> int:
        if(len(triangle) == 0):
            return 0
        n = len(triangle)
        min_sum = [0] * n
        min_sum[0] = triangle[0][0]
        for i in range(1, n, 1):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, i, 1):
                triangle[i][j] += min(triangle[i - 1][j - 1],
                                      triangle[i - 1][j])
            triangle[i][i] += triangle[i - 1][i - 1]
        return min(triangle[n - 1])


s = Solution()
nums = [
     [2]
]
print(s.minimumTotal(nums))
