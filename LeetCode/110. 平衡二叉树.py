# 110. 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:

# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:

# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
import tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def setLeft(self, x):
        self.left = x

    def setRight(self, x):
        self.right = x

    def setVal(self, x):
        self.val = x


class Solution:
    def isBalanced(self, root: TreeNode):
        if(root is None):
            return (True, 0)
        isLeftBalanced, leftHeight = self.isBalanced(root.left)
        isRightBalanced, rightHeight = self.isBalanced(root.right)
        if(isLeftBalanced and
           isRightBalanced and
           abs(leftHeight - rightHeight) <= 1):
            return (True, max(leftHeight, rightHeight) + 1)
        else:
            return (False, max(leftHeight, rightHeight) + 1)


def main():
    t = tree.Tree()
    num = [1, 2, 3, 4, 5, 6]
    t.buildTree(num)
    s = Solution()
    print(s.isBalanced(t.getRoot())[0])


main()
