# 给定一个二叉树，原地将它展开为一个单链表。

#  

# 例如，给定二叉树

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from LeetCode.tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten(root: TreeNode):
            if(root.left is None):
                if(root.right is None):
                    return root
                else:
                    return flatten(root.right)
            else:
                if(root.right is None):
                    root.right = root.left
                    root.left = None
                    return flatten(root.right)
                else:
                    right = root.right
                    root.right = root.left
                    root.left = None
                    left = flatten(root.right)
                    left.left = None
                    left.right = right
                    return flatten(right)
        if(root is None):
            return
        return flatten(root)


if __name__ == '__main__':
    soultion = Solution()
