# 二叉搜索树中的两个节点被错误地交换。

# 请在不改变其结构的情况下，恢复这棵树。

# 示例 1:

# 输入: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# 输出: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# 示例 2:

# 输入: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# 输出: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# 进阶:

# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from LeetCode.tree import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.t1 = None
        self.t2 = None
        self.pre = None
        self.inOrder(root)
        self.t1.val, self.t2.val = self.t2.val, self.t1.val

    def inOrder(self, root: TreeNode):
        if root is None:
            return
        self.inOrder(root.left)
        if self.pre is None:
            self.pre = root
        else:
            if self.pre.val > root.val:
                if self.t1 is None:
                    self.t1 = self.pre
                self.t2 = root
        self.pre = root
        self.inOrder(root.right)
