# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        head, tail = None, None
        index = [i for i in range(len(lists))]
        del_index = []
        for i in index:
            if(lists[i] is None):
                del_index.append(i)
        for i in del_index:
            del(index[i])
        if(len(index) == 0):
            return None
        node = lists[index[0]]
        minn = node.val
        index_ = 0
        for i in index:
            if(lists[i].val < minn):
                index_ = i
                node = lists[i]
                minn = node.val
        head, tail = node, node
        lists[index_] = node.next
        if(lists[index_] is None):
            del(index[index_])

        while(len(index) != 0):
            node = lists[index[0]]
            minn = node.val
            index_ = 0
            for i in index:
                if(lists[i].val < minn):
                    index_ = i
                    node = lists[i]
                    minn = node.val
            tail.next = node
            tail = node
            lists[index_] = node.next
            if(lists[index_] is None):
                del(index[index_])
        tail.next = None
        return head


if __name__ == '__main__':
    s = Solution()
    lists = [1, 2, 3]
    s.mergeKLists(lists)
