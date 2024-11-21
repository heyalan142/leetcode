from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
def max_depth(root: TreeNode) -> int:
    level = 0
    if not root:
        return level
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1


# 迭代法
# def max_depth(root: TreeNode) -> int:
#     if not root:
#         return 0
#     queue = deque()
#     queue.append(root)
#     level = 0
#     while queue:
#         level += 1
#         size = len(queue)
#         for i in range(size):
#             node = queue.popleft()
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return level


if __name__ == '__main__':
    sub_left = TreeNode(2)
    sub_left.left = TreeNode(4)
    sub_left.right = TreeNode(5)
    sub_right = TreeNode(3)
    sub_right.left = TreeNode(6)
    sub_right.right = TreeNode(7)
    tree = TreeNode(1)
    tree.left = sub_left
    tree.right = sub_right
    print(max_depth(tree))
