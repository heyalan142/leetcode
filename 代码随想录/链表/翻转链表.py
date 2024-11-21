class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# 双指针法
def reverseList(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

# 递归法
# def reverse(pre: ListNode, cur: ListNode) -> ListNode:
#     if cur == None:
#         return pre
#
#     temp = cur.next
#     cur.next = pre
#     return reverse(cur, temp)
#
#
# def reverseList(head: ListNode) -> ListNode:
#     pre = None
#     cur = head
#     return reverse(pre, cur)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)

    reverseHead = reverseList(head)
    current = reverseHead
    while current:
        print(current.value)
        current = current.next
