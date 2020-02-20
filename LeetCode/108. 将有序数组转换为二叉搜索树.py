# 108. 将有序数组转换为二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定有序数组: [-10,-3,0,5,9],

# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5


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
    def sortedArrayToBST(self, nums):
        if(len(nums) == 0):
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def main():
    num = [1, 2, 3, 9]
    t = tree.Tree()
    # t.buildTree(num)
    s = Solution()
    t.setRoot(s.sortedArrayToBST(num))
    print(t.levelOrderBottom())


main()
