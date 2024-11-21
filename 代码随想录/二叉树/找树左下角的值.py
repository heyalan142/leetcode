from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = None
        self.max_depth = float('-inf')

    # 迭代法
    def find_bottom_left_value(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result = node.value
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    # 递归法
    # def find_bottom_left_value(self, root: TreeNode) -> int:
    #     self.traversal(root, 0)
    #
    # # 中序遍历
    # def traversal(self, root: TreeNode, depth: int) -> None:
    #     if not root.left and root.right:
    #         if depth > self.max_depth:
    #             self.max_depth = depth
    #             self.result = root.val
    #         return
    #     if root.left:
    #         depth += 1
    #         self.traversal(root.left, depth)
    #         depth -= 1
    #     if root.right:
    #         depth += 1
    #         self.traversal(root.right, depth)
    #         depth -= 1


if __name__ == '__main__':
    sub_left = TreeNode(2)
    sub_left.left = TreeNode(4)
    sub_right = TreeNode(3)
    sub_right.left = TreeNode(5)
    sub_right.right = TreeNode(6)
    sub_right.left.left = TreeNode(7)
    tree = TreeNode(1)
    tree.left = sub_left
    tree.right = sub_right
    solution = Solution()
    print(solution.find_bottom_left_value(tree))
