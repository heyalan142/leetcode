class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == q or root == p:
            return root
        left_result = self.lowest_common_ancestor(self, root.left, p, q)
        right_result = self.lowest_common_ancestor(self.root.right, p, q)
        if left_result and not right_result:
            return left_result
        elif right_result and not left_result:
            return right_result
        elif right_result and left_result:
            return root
        else:
            return None


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(2)
    solution = Solution()
    solution.search_bst(tree)
    print(solution.result)
