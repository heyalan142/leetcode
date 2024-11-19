
'''
https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?
tpId=13&tqId=23286&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
快慢指针法，需要pre指针和cur指针，记得需要temp保存cur.next
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    Solution().reverseList(node1)
