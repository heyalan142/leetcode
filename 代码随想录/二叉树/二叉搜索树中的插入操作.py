class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def insert_to_bst(self, root: TreeNode, value: int) -> TreeNode:
        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert_to_bst(root.left)
        elif value > root.value:
            root.right = self.insert_to_bst(root.right)
        return root
