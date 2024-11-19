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
