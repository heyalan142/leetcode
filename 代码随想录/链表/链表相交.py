class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    lenA = 0
    lenB = 0
    current = headA
    while current:
        lenA += 1
        current = current.next
    current = headB
    while current:
        lenB += 1
        current = current.next

    currentA = headA
    currentB = headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            currentA = currentA.next
    elif lenA < lenB:
        for i in range(lenB - lenA):
            currentB = currentB.next

    while currentA and currentB:
        if currentA == currentB:
            return currentB
        currentA = currentA.next
        currentB = currentB.next
    return None


if __name__ == '__main__':
    nums = [2, 4]
    head = None
    for value in nums[::-1]:
        head = ListNode(value, head)
    numsA = [0, 9, 1]
    headA = None
    for value in nums[::-1]:
        headA = ListNode(value, head)
    numsB = [3]
    headB = None
    for value in numsB[::-1]:
        headB = ListNode(value, head)

    result = getIntersectionNode(headA, headB)
    while result:
        print(result.value)
        result = result.next
