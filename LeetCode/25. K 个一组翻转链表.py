# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

#  

# 示例：

# 给你这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

#  

# 说明：

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
from ListNode import ListNode, List


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, node, nextt = 0, head, None
        tailOne = None
        headTwo = None
        tailTwo = None
        while(node is not None):
            if(count < k):
                nextt = node.next
                node.next = headTwo
                headTwo = node
                if(tailTwo is None):
                    tailTwo = headTwo
                node = nextt
                count += 1
            else:
                if(tailOne is None):
                    tailOne = tailTwo
                    head = headTwo
                else:
                    tailOne.next = headTwo
                    tailOne = tailTwo
                count = 0
                tailTwo = headTwo = None
        if(tailOne is None):
            return headTwo
        if(tailOne is not tailTwo and tailTwo is not None):
            tailOne.next = headTwo
            tailOne = tailTwo
        tailOne.next = None
        return head

    def reverseKGroupKeep(self, head: ListNode, k: int) -> ListNode:
        count = 1
        tail = None
        node, start, end = head, head, head
        while(node is not None):
            if(count == k):
                end = node
                node = node.next
                if(start is not end):
                    last = start
                    temp = start.next
                    while(temp is not end):
                        nextt = temp.next
                        temp.next = last
                        last = temp
                        temp = nextt
                    end.next = last
                start, end = end, start
                if(tail is None):
                    head = start
                    tail = end
                else:
                    tail.next = start
                    tail = end
                start = end = node
                count = 1
            else:
                node = node.next
                count += 1
        if(tail is None):
            return head
        tail.next = start
        return head


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = List.getHead(nums)
    # List.printList(head)
    s = Solution()
    head = s.reverseKGroupKeep(head, 6)
    List.printList(head)
    pass
