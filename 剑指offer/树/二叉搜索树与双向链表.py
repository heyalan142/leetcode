'''
https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?
tpId=13&tqId=23253&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
二叉搜索树最左端的元素一定最小，最右端的元素一定最大，符合“左中右”的特性，因此二叉搜索树的中序遍历就是一个递增序列，我们只要对它中序遍历就可以组装称为递增双向链表。

具体做法：
step 1：创建两个指针，一个指向题目中要求的链表头（head），一个指向当前遍历的前一节点（pre)。
step 2：首先递归到最左，初始化head与pre。
step 3：然后处理中间根节点，依次连接pre与当前节点，连接后更新pre为当前节点。
step 4：最后递归进入右子树，继续处理。
step 5：递归出口即是节点为空则返回。
'''


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
            # 关键代码：注意返回的左链表的头部，但是串的是左链表的尾部
            while current.next:
                current = current.next
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
