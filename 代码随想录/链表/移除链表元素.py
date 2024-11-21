class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_elements(head: ListNode, target: int) -> ListNode:
    dump_head = ListNode(0, head)
    current = dump_head
    while current.next:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next
    return dump_head.next


if __name__ == '__main__':
    nums = [1, 2, 6, 3, 4, 5, 6]
    head = None
    for value in nums[::-1]:
        head = ListNode(value, head)
    target = 6
    result = remove_elements(head, target)
    while result:
        print(result.value)
        result = result.next
