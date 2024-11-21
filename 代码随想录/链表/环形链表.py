class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


if __name__ == '__main__':
    nums = [3, 2, 0, -4]
    head = None
    for num in reversed(nums):
        head = ListNode(num, head)

    current = head
    while current.next:
        current = current.next
    current.next = head.next

    result = detectCycle(head)
