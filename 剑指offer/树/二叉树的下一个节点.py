
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
