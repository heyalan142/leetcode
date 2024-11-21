from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_bottom_order(root: TreeNode) -> list[list[int]]:
    results = []
    if root is None:
        return results
    queue = deque()
    node = root
    queue.append(node)
    while queue:
        result = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        results.append(result)
    return results[::-1]


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
    print(level_bottom_order(tree))
