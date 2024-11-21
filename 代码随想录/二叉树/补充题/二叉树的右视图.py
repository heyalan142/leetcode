from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.right:
            queue.append(node.right)
    return result


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
    print(right_side_view(tree))
