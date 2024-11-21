from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 递归法
# def get_count(root: TreeNode) -> int:
#     if not root:
#         return 0
#     left_num = get_num(root.left)
#     right_num = get_num(root.right)
#     return left_num + right_num + 1

# 迭代法
def get_count(root: TreeNode) -> int:
    if not root:
        return 0
    count = 0
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count


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
    result = get_count(tree)
    print(result)
