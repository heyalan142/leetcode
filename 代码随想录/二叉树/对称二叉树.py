
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


# 递归法
def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return is_compare(root.left, root.right)


def is_compare(left: TreeNode, right: TreeNode) -> bool:
    if not right and not left:
        return True
    if not right and left:
        return False
    if not left and right:
        return False
    if left.value != right.value:
        return False
    isOutSame = is_compare(left.left, right.right)
    isInsideSame = is_compare(left.right, right.left)
    return isOutSame and isInsideSame


# 迭代法
# def is_symmetric(root: TreeNode) -> bool:
#     if not root:
#         return True
#
#     queue = deque([root.left, root.right])
#
#     while queue:
#         level_size = len(queue)
#         if level_size % 2 != 0:
#             return False
#         level_vals = []
#         for i in range(level_size):
#             node = queue.popleft()
#             if node:
#                 level_vals.append(node.value)
#                 queue.append(node.left)
#                 queue.append(node.right)
#             else:
#                 level_vals.append(None)
#
#         if level_vals != level_vals[::-1]:
#             return False
#
#     return True


if __name__ == '__main__':
    sub_left = TreeNode(2)
    sub_left.left = TreeNode(3)
    sub_left.right = TreeNode(4)
    sub_right = TreeNode(2)
    sub_right.left = TreeNode(4)
    sub_right.right = TreeNode(3)
    tree = TreeNode(1)
    tree.left = sub_left
    tree.right = sub_right
    print(is_symmetric(tree))
