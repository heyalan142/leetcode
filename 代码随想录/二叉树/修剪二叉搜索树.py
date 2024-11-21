class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def trim_bst(self, root: TreeNode, low_limit: int, high_limit: int) -> TreeNode:
        if not root:
            return None

        if root.value < low_limit:
            return self.trim_bst(root.right, low_limit, high_limit)
        if root.right.value > high_limit:
            return self.trim_bst(root.left, low_limit, high_limit)

        else:
            root.left = self.trim_bst(root.left, low_limit, high_limit)
            root.right = self.trim_bst(root.right, low_limit, high_limit)
            return root
