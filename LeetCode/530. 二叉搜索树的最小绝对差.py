# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

#  

# 示例：

# 输入：

#    1
#     \
#      3
#     /
#    2

# 输出：
# 1

# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#  

# 提示：

# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from LeetCode.tree import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.last = None
        self.min = float('inf')
        self.getMin(root)
        return self.min

    def getMin(self, root: TreeNode):
        if root is None:
            return
        self.getMin(root.left)
        if self.last is not None:
            diff = abs(root.val - self.last)
            if diff < self.min:
                self.min = diff
        self.last = root.val
        self.getMin(root.right)
