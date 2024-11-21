class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
def search_bst(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return None
    if target == root.value:
        return root
    elif target < root.value:
        return search_bst(root.left, target)
    elif target > root.value:
        return search_bst(root.left, target)

# 迭代法
# def search_bst(root: TreeNode, target: int) -> TreeNode:
#     while root:
#         if target == root.value:
#             return root
#         elif target > root.value:
#             root = root.left
#         elif target < root.value:
#             root = root.right
#     return None
