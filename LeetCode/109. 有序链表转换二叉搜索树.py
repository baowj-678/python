# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from LeetCode.tree import TreeNode
from LeetCode.ListNode import ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def step(head, tail):
            if head == tail:
                if head is None:
                    return None
                else:
                    return TreeNode(val=head.val)
            fast, slow, last_slow = head.next, head, None
            while fast != tail:
                fast = fast.next
                if fast == tail:
                    break
                fast = fast.next
                last_slow = slow
                slow = slow.next
            Node = None
            if tail is None:
                Node = TreeNode(slow.val)
                Node.right = step(slow.next, tail)
                if last_slow is None:
                    Node.left = None
                else:
                    Node.left = step(head, last_slow)
            else:
                last_slow = slow
                slow = slow.next
                Node = TreeNode(slow.val)
                if slow != tail:
                    Node.right = step(slow.next, tail)
                else:
                    Node.right = None
                Node.left = step(head, last_slow)
            return Node
        return step(head, None)
