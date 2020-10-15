# 给定一个二叉树

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

#  

# 进阶：

# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a Node.
import queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        Q = queue.Queue()
        Q.put(None)
        now_node = root
        if root is None:
            return
        while Q.empty() is False:
            next_node = Q.get()
            if now_node is None:
                Q.put(None)
            else:
                now_node.next = next_node
                left = now_node.left
                right = now_node.right
                if left is not None:
                    Q.put(left)
                if right is not None:
                    Q.put(right)
            now_node = next_node
        return root
