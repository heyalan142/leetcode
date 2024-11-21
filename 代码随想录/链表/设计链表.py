class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# 获取某个节点的值
def get(index: int, head: ListNode) -> int:
    dummy_head = ListNode(0, head)
    current = dummy_head
    i = 0
    while current.next:
        if i == index:
            return current.next.value
        current = current.next
        i += 1
    return -1


# 在最前面增加节点
def addAtHead(value: int, head: ListNode) -> ListNode:
    dummy_head = ListNode(0, head)
    current = ListNode(value, dummy_head.next)
    dummy_head.next = current
    return current


# 在最后面增加节点
def addAtTail(value: int, head: ListNode) -> ListNode:
    dummy_head = ListNode(0, head)
    current = dummy_head
    while current.next:
        current = current.next
    current.next = ListNode(value)
    return dummy_head


# 在index处增加节点
def addAtIndex(value: int, index: int, head: ListNode) -> ListNode:
    dummy_head = ListNode(0, head)
    current = dummy_head
    i = 0
    while current.next:
        if i == index:
            node = ListNode(value)
            node.next = current.next
            current.next = node
        i += 1
        current = current.next
    return dummy_head


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6]
    head = None
    for value in nums[::-1]:
        head = ListNode(value, head)
    # print(get(4, head))
    # head = addAtHead(0, head)
    # head = addAtTail(6, head)
    head = addAtIndex(3, 2, head)
    while head.next:
        print(head.next.value)
        head = head.next
