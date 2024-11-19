from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def findPath(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return self.res
            # 查询以某节点为根的路径数
        self.findTarget(root, sum)
        # 以其子节点为新根
        self.findPath(root.left, sum)
        self.findPath(root.right, sum)
        return self.res

    def findTarget(self, root: TreeNode, sum: int):
        if root is None:
            return
        # 符合目标值
        if sum == root.val:
            self.res += 1
        # 进入子节点继续找
        self.findTarget(root.left, sum - root.val)
        self.findTarget(root.right, sum - root.val)


if __name__ == '__main__':
    pRoot = TreeNode(0)
    pRoot.left = TreeNode(1)
    pRoot.right = TreeNode(1)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().findPath(pRoot, 1)
    print(results)
