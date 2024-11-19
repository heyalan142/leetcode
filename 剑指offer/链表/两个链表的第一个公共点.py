
'''
https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?
tpId=13&tqId=23267&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
先分别求两个链表的长度，让长的链表先走len(B) - len(A)步，然后再同时走。两指针就会在某一个点相遇！
这个相遇点就是我们要找的第一个公共节点。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findFirstCommonNode(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        length1 = self.getLength(pHead1)
        length2 = self.getLength(pHead2)
        current1 = pHead1
        current2 = pHead2
        if length1 > length2:
            current1 = self.moveForward(length1 - length2, pHead1)
        elif length1 < length2:
            current2 = self.moveForward(length2 - length1, pHead2)
        while current1 and current2:
            if current1 == current2:
                return current1
            current1 = current1.next
            current2 = current2.next
        return None

    def moveForward(self, steps: int, pHead: ListNode) -> ListNode:
        current = pHead
        for i in range(steps):
            current = current.next
        return current

    def getLength(self, pHead: ListNode) -> int:
        totalLength = 0
        current = pHead
        while current:
            totalLength += 1
            current = current.next
        return totalLength


if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)

    node4 = ListNode(4)
    node5 = ListNode(5)

    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node6
    node6.next = node7

    node4.next = node5
    node5.next = node6
    node6.next = node7

    current = Solution().findFirstCommonNode(node1, node4)
    while current:
        print(current.val)
        current = current.next


