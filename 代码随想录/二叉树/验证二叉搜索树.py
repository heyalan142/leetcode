class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None  # 用来记录前一个节点

    def is_valid_bst(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_valid = self.is_valid_bst(root.left)
        if self.pre is not None and self.pre.value >= root.value:
            return False
        self.pre = root  # 记录前一个节点
        right_valid = self.is_valid_bst(root.right)
        return left_valid and right_valid


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    solution = Solution()
    print(solution.is_valid_bst(tree))

    # sub_left = TreeNode(1)
    # sub_right = TreeNode(4)
    # sub_right.left = TreeNode(3)
    # sub_right.right = TreeNode(6)
    # tree = TreeNode(5)
    # tree.left = sub_left
    # tree.right = sub_right
    # solution = Solution()
    # print(solution.is_valid_bst(tree))
