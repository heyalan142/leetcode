from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
def min_depth(node: TreeNode) -> int:
    if not node:
        return 0
    left_depth = min_depth(node.left)
    right_depth = min_depth(node.right)
    # 当一个左子树为空，右不为空，这时并不是最低点
    if node.left is None and node.right is not None:
        return 1 + right_depth

    # 当一个右子树为空，左不为空，这时并不是最低点
    if node.left is not None and node.right is None:
        return 1 + left_depth

    result = 1 + min(left_depth, right_depth)
    return result

# 迭代法
# def min_depth(root: TreeNode) -> int:
#     if not root:
#         return 0
#     queue = deque()
#     queue.append(root)
#     result = 0
#     while queue:
#         size = len(queue)
#         result += 1
#         for i in range(size):
#             node = queue.popleft()
#             if not node.left and not node.right:
#                 return result
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return result


if __name__ == '__main__':
    sub_left = TreeNode(9)
    sub_right = TreeNode(20)
    sub_right.left = TreeNode(15)
    sub_right.right = TreeNode(7)
    tree = TreeNode(3)
    tree.left = sub_left
    tree.right = sub_right
    print(min_depth(tree))
