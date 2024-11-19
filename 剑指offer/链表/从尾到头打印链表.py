
'''
https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?
tpId=13&tqId=23278&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printListFromTailToHead(self, listNode: ListNode) -> list[int]:
        node = listNode
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        nums.reverse()
        return nums


if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    print(Solution().printListFromTailToHead(node1))
