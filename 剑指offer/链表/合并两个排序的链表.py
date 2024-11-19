'''
https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?
tpId=13&tqId=23267&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
新建一个phead3链表，一个一个的比较pHead1和pHead2的大小串到phead3链表上
遍历到最后肯定有一个链表还有剩余的节点，它们的值将大于前面所有的，直接连在新的链表后面即可
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        cur1 = pHead1
        cur2 = pHead2
        phead3 = ListNode(-1)
        cur3 = phead3
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
            cur3 = cur3.next
        # 关键代码：记得串最后剩下的一个节点
        cur3.next = cur1 if cur1 else cur2
        return phead3.next


if __name__ == '__main__':
    node5 = ListNode(5)
    node3 = ListNode(4, node5)
    node1 = ListNode(1, node3)

    node6 = ListNode(6)
    node4 = ListNode(3, node6)
    node2 = ListNode(2, node4)
    Solution().merge(node1, node2)
