'''
https://github.com/youngyangyang04/leetcode-master/blob/master/problems
/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md
'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def swap_pairs(node: ListNode) -> ListNode:
    dump_head = ListNode(0, node)
    current = dump_head
    while current.next and current.next.next:
        temp1 = current.next
        temp2 = current.next.next.next
        current.next = current.next.next
        current.next.next = temp1
        temp1.next = temp2
        current = current.next.next
    return dump_head.next


if __name__ == '__main__':
    nums = [2, 1, 4, 3]
    head = None
    for value in nums[::-1]:
        head = ListNode(value, head)
    result = swap_pairs(head)
    while result:
        print(result.value)
        result = result.next
