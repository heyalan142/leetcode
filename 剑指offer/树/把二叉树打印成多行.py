from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printLines(self, pRoot: TreeNode) -> list[list[int]]:
        results = []
        if pRoot is None:
            return results
        queue = deque()
        queue.append(pRoot)
        while queue:
            result = []
            for i in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(result)
        return results


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().printLines(pRoot)
    print(results)
