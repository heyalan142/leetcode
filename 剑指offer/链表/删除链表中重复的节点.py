
'''
https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?
tpId=13&tqId=23450&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
这是一个升序链表，重复的节点都连在一起，我们就可以很轻易地比较到重复的节点，然后将所有的连续相同的节点都跳过，
连接不相同的第一个节点
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        if pHead is None:
            return None
        dump = ListNode(0, pHead)
        cur = dump
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next.val
                # 关键代码：不能只删一个，要遍历全部删完
                while cur.next is not None and cur.next.val == temp:
                    cur.next = cur.next.next
                # 关键代码
            else:
                cur = cur.next
        return dump.next


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 4, 5]
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)
    phead = Solution().deleteDuplication(head)
    current = phead
    while current:
        print(current.val)
        current = current.next
