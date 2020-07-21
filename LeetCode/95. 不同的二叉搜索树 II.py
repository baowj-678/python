# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

#  

# 示例：

# 输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  

# 提示：

# 0 <= n <= 8

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from tree import TreeNode


class Solution:
    def generateTrees(self, n: int):
        def generateTrees(left, right):
            Trees = []
            if(left == right):
                Trees.append(TreeNode(left))
            elif(left > right):
                Trees.append(None)
            else:
                for i in range(left, right + 1, 1):
                    leftTrees = generateTrees(left, i - 1)
                    rightTrees = generateTrees(i + 1, right)
                    for leftTree in leftTrees:
                        for rightTree in rightTrees:
                            tmp = TreeNode(i)
                            tmp.left = leftTree
                            tmp.right = rightTree
                            Trees.append(tmp)
            return Trees
        if(n == 0):
            return []
        return generateTrees(1, n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateTrees(2))
