
'''
https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?
tpId=13&tqId=23449&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
快慢指针，快指针每次走两步，慢指针每次走一步，相遇后慢指针回头部，快指针继续往前每次走一步，快慢指针再次相遇即为环入口节点
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def entryNodeOfLoop(self, pHead) -> ListNode:
        slow = pHead
        fast = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = pHead
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
