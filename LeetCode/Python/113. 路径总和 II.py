# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from LeetCode.tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:
        self.ans = []
        self.findSum(root, [], sum)
        return self.ans

    def findSum(self, root: TreeNode, sum_: list, target):
        if root is None:
            return
        target -= root.val
        sum_.append(root.val)
        if target == 0:
            if root.left is None and root.right is None:
                self.ans.append(sum_.copy())
            else:
                self.findSum(root.left, sum_, target)
                self.findSum(root.right, sum_, target)
        else:
            self.findSum(root.left, sum_, target)
            self.findSum(root.right, sum_, target)
        sum_.pop()
