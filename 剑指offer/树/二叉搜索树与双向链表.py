class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.font = None
        self.next = None


'''
# 左子树生成链表尾巴串中节点串右子树生成链表头部
'''


class Solution:
    def convert(self, pRootOfTree: TreeNode) -> ListNode:
        head = None
        if pRootOfTree is None:
            return head
        node = ListNode(pRootOfTree.val)
        head = node
        if pRootOfTree.left:
            leftConvert = self.convert(pRootOfTree.left)
            current = leftConvert
            '''
            # 关键代码：注意返回的左链表的头部，但是串的是左链表的尾部
            '''
            while current.next:
                current = current.next
            '''
             # 关键代码
            '''
            current.next = node
            node.font = current
            head = leftConvert
        if pRootOfTree.right:
            rightConvert = self.convert(pRootOfTree.right)
            node.next = rightConvert
            rightConvert.font = node
        return head


if __name__ == '__main__':
    pRoot = TreeNode(10)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(14)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(8)
    pRoot.right.left = TreeNode(12)
    pRoot.right.right = TreeNode(16)
    listNode = Solution().convert(pRoot)
    print(listNode)
