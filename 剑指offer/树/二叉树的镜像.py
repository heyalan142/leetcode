class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror(self, pRoot: TreeNode) -> TreeNode:
        if pRoot is None:
            return None
        leftMirror = self.mirror(pRoot.left)
        rightMirror = self.mirror(pRoot.right)
        pRoot.left = rightMirror
        pRoot.right = leftMirror
        return pRoot




if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    mirror = Solution().mirror(pRoot)
    print(mirror)
