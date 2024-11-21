class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float('inf')  # 用来记录前一个节点
        self.pre = None

    def traversal(self, root: TreeNode) -> None:
        if not root:
            return
        self.traversal(root.left)
        if self.pre is not None:  # 中
            self.result = min(self.result, root.value - self.pre.value)
        self.pre = root  # 记录前一个节点
        self.traversal(root.right)

    def min_abs_distance(self, root: TreeNode) -> int:
        self.traversal(root)
        return self.result


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(2)
    solution = Solution()
    print(solution.min_abs_distance(tree))

