class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.pre_node = None

    def delete_one_node(self, target: TreeNode) -> TreeNode:
        if not target:
            return None
        if not target.right:
            return target.left
        current = target.right
        while current.left:
            current = current.left
        current.left = target.left
        return target.right

    def delete_node(self, root: TreeNode, value: int) -> TreeNode:
        if not root:
            return None
        current = root
        while current:
            if value == current.value:
                break
            self.pre_node = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if not self.pre_node:
            self.delete_one_node(current)
        elif self.pre_node.left.value == value:
            self.pre_node.left = self.delete_one_node(current)
        elif self.pre_node.right.value == value:
            self.pre_node.right = self.delete_one_node(current)
