'''
https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?
tpId=13&tqId=23265&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
思路：
将小朋友装入一个头尾衔接的链表。 遇到满足条件的删除节点即可。

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def LastRemaining_Solution(self, n: int, m: int) -> int:
        head = self.buildCyclelinked(range(n))
        current = head
        index = 1
        while current != current.next:
            if index == m - 1 or m == 1:
                current.next = current.next.next
                current = current.next
                index = 1
            else:
                current = current.next
                index += 1
        return current.val

    def buildCyclelinked(self, source: list[int]):
        head = ListNode(source[0], None)
        current = head
        for num in reversed(source[1:]):
            current = ListNode(num, current)
        head.next = current
        return head


if __name__ == '__main__':
    val = Solution().LastRemaining_Solution(10, 17)
    print(val)
