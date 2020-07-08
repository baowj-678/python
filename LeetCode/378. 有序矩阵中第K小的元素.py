# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

#  

# 示例：

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# 返回 13。
#  

# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while(left < right):
            mid = (left + right) // 2
            cut = self.count(matrix, mid)
            if(cut < k):
                left = mid + 1
            else:
                right = mid
        return left

    def count(self, matrix, mid):
        num = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] <= mid):
                    num += 1
        return num


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,  5,  9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    print(solution.kthSmallest(matrix, k))
