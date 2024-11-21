from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
def traversal(root: TreeNode) -> list[str]:
    if not root:
        return []
    left_traversal = traversal(root.left)
    right_traversal = traversal(root.right)
    results = []
    if len(left_traversal) <= 0 and len(right_traversal) <= 0:
        result = str(root.value)
        results.append(result)

    if len(left_traversal) > 0:
        for string in left_traversal:
            result = str(root.value) + "->" + string
            results.append(result)

    if len(right_traversal) > 0:
        for string in right_traversal:
            result = str(root.value) + "->" + string
            results.append(result)
    return results

# 迭代法
# def traversal(root: TreeNode) -> list[str]:
#     if not root:
#         return []
#     paths = [str(root.value)]
#     stack = [root]
#     results = []
#     while stack:
#         node = stack.pop()
#         path = paths.pop()
#         if not node.left and not node.right:
#             results.append(path)
#         if node.right:
#             stack.append(node.right)
#             path_right = path + '->' + str(node.right.value)
#             paths.append(path_right)
#         if node.left:
#             stack.append(node.left)
#             path_left = path + '->' + str(node.left.value)
#             paths.append(path_left)
#     return results


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
    print(traversal(tree))
