# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from LeetCode.tree import TreeNode


class Solution:
    def buildTree(self, inorder, postorder: list) -> TreeNode:
        self.postorder = postorder
        return self.generateTree(inorder)

    def generateTree(self, inorder):
        if len(inorder) == 0:
            return None
        node = TreeNode()
        node.val = self.postorder[-1]
        self.postorder.pop()
        splitPoint = None
        for i in range(len(inorder)):
            if inorder[i] == node.val:
                splitPoint = i
        node.right = self.generateTree(inorder[splitPoint + 1:])
        node.left = self.generateTree(inorder[0: splitPoint])
        return node
