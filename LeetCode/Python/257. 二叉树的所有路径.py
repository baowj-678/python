# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 输入:

#    1
#  /   \
# 2     3
#  \
#   5

# 输出: ["1->2->5", "1->3"]

# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from LeetCode.tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root is None:
            return []
        ans = []
        s = str(root.val)
        if root.left is not None:
            self.findPath(root.left, ans, s)
        s = str(root.val)
        if root.right is not None:
            self.findPath(root.right, ans, s)
        if len(ans) == 0:
            ans.append(s)
        return ans

    def findPath(self, root: TreeNode, ans: list, s: str):
        if root.left is None and root.right is None:
            s = s + '->' + str(root.val)
            ans.append(s)
        else:
            s = s + '->' + str(root.val)
            if root.left is not None:
                self.findPath(root.left, ans, s)
            if root.right is not None:
                self.findPath(root.right, ans, s)
        return
