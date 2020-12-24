# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from tree import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode):
        cur = TreeNode()
        ans = []
        cur.left = root
        while cur is not None:
            left = cur.left
            if left is None:
                cur = cur.right
            else:
                while left.right is not None:
                    left = left.right
                pre = left
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    tmp = []
                    tmp_p = cur.left
                    while tmp_p is not pre:
                        tmp.append(tmp_p.val)
                        tmp_p = tmp_p.right
                    tmp.append(pre.val)
                    pre.right = None
                    cur = cur.right
                    ans += tmp.reverse()
        return ans
