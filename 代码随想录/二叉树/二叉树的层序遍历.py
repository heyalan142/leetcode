from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root: TreeNode):
    results = []
    if root is None:
        return results
    queue = deque()
    queue.append(root)
    while queue:
        result = []
        for i in range(len(queue)):
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        results.append(result)
    return results


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
    print(level_order(tree))
