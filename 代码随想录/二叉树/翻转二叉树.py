from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    invert_tree(root.left)
    invert_tree(root.right)
    return root

# 迭代法
# def invert_tree(root: TreeNode) -> TreeNode:
#     if root is None:
#         return None
#     queue = deque()
#     queue.append(root)
#     while queue:
#         node = queue.popleft()
#         if node.left and node.right:
#             temp = node.left
#             node.left = node.right
#             node.right = temp
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return root


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
    root = invert_tree(tree)
    print("f")
