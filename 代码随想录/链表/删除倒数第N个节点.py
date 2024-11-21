class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummyHead = ListNode(0, head)
    slow = dummyHead
    fast = dummyHead

    # 快指针比慢指针快 n+1 步,n+1不是n因为慢指针必须指向删除节点的前一个节点
    for i in range(n+1):
        fast = fast.next

    # 移动两个指针，直到快速指针到达链表的末尾
    while fast:
        slow = slow.next
        fast = fast.next

    # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
    slow.next = slow.next.next
    return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2]
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)

    head = removeNthFromEnd(head, 1)
    current = head
    while current:
        print(current.value)
        current = current.next
