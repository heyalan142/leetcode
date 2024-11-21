class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.pre = 0

    def traversal(self, root: TreeNode) -> None:
        if not root:
            return
        self.traversal(root.right)
        root.value += self.pre
        self.pre = root.value
        self.traversal(root.left)

    def covert_bst(self, root: TreeNode) -> TreeNode:
        self.traversal(root)
        return root

    def generate_bst(self, nums: [int]) -> TreeNode:
        if len(nums) <= 0:
            return None
        middel_index = len(nums) // 2
        value = nums[middel_index]
        root = TreeNode(value)
        left_nums = nums[:middel_index]
        right_nums = nums[middel_index + 1:]
        root.left = self.generate_bst(left_nums)
        root.right = self.generate_bst(right_nums)
        return root


if __name__ == '__main__':
    nums = [4, 1, 6, 0, 2, 5, 7, 3, 8]
    nums.sort()
    solution = Solution()
    tree1 = solution.generate_bst(nums)
    tree2 = solution.covert_bst(tree1)
    print("")
