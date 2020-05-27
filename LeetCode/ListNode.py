class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self):
        pass

    def getHead(nums) -> ListNode:
        if(len(nums) == 0):
            return None
        temp = ListNode(nums[0])
        head = tail = temp
        for i in nums[1:]:
            temp = ListNode(i)
            tail.next = temp
            tail = temp
        tail.next = None
        return head

    def printList(head):
        while(head is not None):
            print(head.val, end='')
            print('->', end='')
            head = head.next
        print('None')
