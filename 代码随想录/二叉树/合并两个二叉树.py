class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def merge_tree(tree1: TreeNode, tree2: TreeNode) -> TreeNode:
    if not tree1:
        return tree2
    if not tree2:
        return tree1
    left_merge_tree = merge_tree(tree1.left, tree2.left)
    right_merge_tree = merge_tree(tree1.right, tree2.right)
    value = tree1.value + tree2.value
    return TreeNode(value, left_merge_tree, right_merge_tree)


