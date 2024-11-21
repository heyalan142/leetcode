class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归遍历
def sum_left_leaves(root: TreeNode) -> int:
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 0
    left_sum = sum_left_leaves(root.left)
    right_sum = sum_left_leaves(root.right)
    if root.left and not root.left.left and not root.left.right:
        left_sum = root.left.value
    return left_sum + right_sum

# 迭代遍历
# def sum_left_leaves(root: TreeNode) -> int:
#     if not root:
#         return 0
#     stack = [root]
#     result = 0
#     while stack:
#         node = stack.pop()
#         if node.left and not node.left.left and not node.left.right:
#             result += node.left.value
#             stack.append(node.right)
#             stack.append(node.left)
#     return result


if __name__ == '__main__':
    sub_left = TreeNode(9)
    sub_right = TreeNode(20)
    sub_right.left = TreeNode(15)
    sub_right.right = TreeNode(7)
    tree = TreeNode(3)
    tree.left = sub_left
    tree.right = sub_right
    print(sum_left_leaves(tree))
