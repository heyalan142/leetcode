'''
https://www.nowcoder.com/practice/f9f78ca89ad643c99701a7142bd59f5d?
tpId=13&tqId=2273171&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        dump = ListNode(0)
        dump.next = head
        cur = dump
        while cur.next and cur.next.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dump.next


if __name__ == '__main__':
    nums = [4, 5, 1, 9]
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)
    phead = Solution().deleteNode(head, 5)
    current = phead
    while current:
        print(current.val)
        current = current.next
