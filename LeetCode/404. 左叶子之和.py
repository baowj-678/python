# 计算给定二叉树的所有左叶子之和。

# 示例：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-left-leaves
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from LeetCode.tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.subFun(root, False)
        return self.sum

    def subFun(self, root, isLeft):
        if root is None:
            return None
        if root.left is None and root.right is None and isLeft:
            self.sum += root.val
        self.subFun(root.left, True)
        self.subFun(root.right, False)
        return None
