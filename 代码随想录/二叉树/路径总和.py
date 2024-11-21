class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # 递归法
    # def traversal(root: TreeNode, target: int) -> bool:
    #     if not root.left and not root.right and target == 0:
    #         return True
    #     if not root.left and not root.right:
    #         return False
    #     if root.left:
    #         target -= root.left.value
    #         if traversal(root.left, target):
    #             return True
    #         target += root.left.value
    #     if root.right:
    #         target -= root.right.value
    #         if traversal(root.right, target):
    #             return True
    #         target += root.right.value
    #     return False

    # 递归法
    # def has_path_sum(root: TreeNode, target: int) -> bool:
    #     if root is None:
    #         return False
    #     return traversal(root, target - root.value)

    # 递归法


def has_path_sum(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and target == root.value:
        return True
    return has_path_sum(root.left, target - root.value) or has_path_sum(root.right, target - root.value)


# 迭代法
# def has_path_sum(root: TreeNode, target: int) -> bool:
#     if root is None:
#         return False
#     stack = [(root, root.value)]
#     while stack:
#         node, path_sum = stack.pop()
#         if not node.left and not node.right and path_sum == target:
#             return True
#         if node.left:
#             stack.append((node.left, path_sum + node.left.value))
#         if node.right:
#             stack.append((node.right, path_sum + node.right.value))
#     return False


if __name__ == '__main__':
    sub_left = TreeNode(9)
    sub_right = TreeNode(20)
    sub_right.left = TreeNode(15)
    sub_right.right = TreeNode(7)
    tree = TreeNode(3)
    tree.left = sub_left
    tree.right = sub_right
    print(has_path_sum(tree, 12))
