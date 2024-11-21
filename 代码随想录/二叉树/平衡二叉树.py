class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 递归法
# def is_balanced(root: TreeNode) -> bool:
#     height = get_height(root)
#     return height != -1


# def get_height(root: TreeNode) -> int:
#     if not root:
#         return 0
#     left_height = get_height(root.left)
#     right_height = get_height(root.right)
#     if left_height == -1 or right_height == -1:
#         return -1
#     elif abs(left_height - right_height) > 1:
#         return -1
#     else:
#         return max(left_height, right_height) + 1

# 迭代法
def is_balanced(root: TreeNode) -> bool:
    height = get_height(root)
    return height != -1


def get_height(root: TreeNode) -> int:
    if not root:
        return 0
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if left_height == -1 or right_height == -1:
        return -1
    elif abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    sub_left = TreeNode(9)
    sub_right = TreeNode(20)
    sub_right.left = TreeNode(15)
    sub_right.right = TreeNode(7)
    tree = TreeNode(3)
    tree.left = sub_left
    tree.right = sub_right
    print(is_balanced(tree))

    # sub_right = TreeNode(2)
    # sub_left = TreeNode(2)
    # sub_left.left = TreeNode(3)
    # sub_left.right = TreeNode(3)
    # sub_left.left.left = TreeNode(4)
    # sub_left.left.right = TreeNode(4)
    # tree = TreeNode(1)
    # tree.left = sub_left
    # tree.right = sub_right
    # print(is_balanced(tree))
