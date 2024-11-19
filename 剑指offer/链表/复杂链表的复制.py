class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def cloneListNode(self, pHead: ListNode) -> ListNode:



if __name__ == '__main__':
    nums = []
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)
    phead = Solution().cloneListNode(head)

    current = phead
    while current:
        print(current.val)
        current = current.next
