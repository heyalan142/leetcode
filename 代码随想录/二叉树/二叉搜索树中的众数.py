class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None  # 用来记录前一个节点
        self.max_count = 0
        self.count = 0
        self.result = []

    def search_bst(self, root: TreeNode) -> None:
        if not root:
            return
        self.search_bst(root.left)
        if self.pre is not None and self.pre.value == root.value:
            self.count += 1
        else:
            self.count = 0
        self.pre = root  # 记录前一个节点
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [root.value]
        elif self.count == self.max_count:
            self.result.append(root.value)
        self.search_bst(root.right)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(2)
    solution = Solution()
    solution.search_bst(tree)
    print(solution.result)
