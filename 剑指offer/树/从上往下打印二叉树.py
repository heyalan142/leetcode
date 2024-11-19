from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# 使用队列，每次取出队列里的第一个树节点，然后把树节点的左右树节点加进去
'''
class Solution:
    def printFromTopToBottom(self, root: TreeNode) -> list[int]:
        results = []
        if root is None:
            return results
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            results.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().printFromTopToBottom(pRoot)
    print(results)
