from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if root is None:
            return -1
        '''
        # 关键终止条件：找到了一个p或者q，任何祖先也是根节点
        '''
        if root.val == p or root.val == q:
            return root.val
        '''
        # 关键终止条件
        '''
        leftAncestor = self.lowestCommonAncestor(root.left, p, q)
        rightAncestor = self.lowestCommonAncestor(root.right, p, q)
        if leftAncestor != -1 and rightAncestor != -1:
            return root.val
        elif leftAncestor != -1:
            return leftAncestor
        elif rightAncestor != -1:
            return rightAncestor
        return -1


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().lowestCommonAncestor(pRoot, 4, 5)
    print(results)
