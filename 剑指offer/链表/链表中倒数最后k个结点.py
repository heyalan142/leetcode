'''
https://www.nowcoder.com/practice/886370fe658f41b498d40fb34ae76ff9?
tpId=13&tqId=1377477&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
快慢指针，快指针每次走两步，快指针先走k步，快慢指针再一起走。快指针走到结尾处，慢指针是倒数第k个
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        slow = pHead
        fast = pHead
        for i in range(k):
            if fast is not None:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    nums = []
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)
    phead = Solution().findKthToTail(head, 2)

    current = phead
    while current:
        print(current.val)
        current = current.next
