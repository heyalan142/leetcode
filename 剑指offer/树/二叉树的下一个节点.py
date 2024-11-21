'''
https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?
tpId=13&tqId=23451&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
思路：
我们首先要根据给定输入中的结点指针向父级进行迭代，直到找到该树的根节点；
然后根据根节点进行中序遍历，当遍历到和给定树节点相同的节点时，下一个节点就是我们的目标返回节点

具体做法：
step 1：首先先根据当前给出的结点找到根节点
step 2：然后根节点调用中序遍历
step 3：将中序遍历结果存储下来
step 4：最终拿当前结点匹配是否有符合要求的下一个结点
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def getNext(self, pNode: TreeLinkNode) -> TreeLinkNode:
        root = pNode
        # 查找根节点
        while root.next:
            root = root.next
        nodes = []
        self.middleOrder(root, nodes)
        for i in range(len(nodes) - 1):
            cur = nodes[i]
            if pNode == cur:
                return nodes[i + 1]
        return None

    def middleOrder(self, root: TreeLinkNode, nodes: list) -> None:
        if root is None:
            return
        self.middleOrder(root.left, nodes)
        nodes.append(root)
        self.middleOrder(root.right, nodes)


if __name__ == '__main__':
    pRoot = TreeLinkNode(1)
    pRoot.left = TreeLinkNode(2)
    pRoot.right = TreeLinkNode(3)
    pRoot.left.left = TreeLinkNode(4)
    pRoot.left.right = TreeLinkNode(5)
    results = Solution().getNext(pRoot)
    print(results)
