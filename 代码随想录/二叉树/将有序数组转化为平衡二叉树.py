class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
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
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    tree = solution.generate_bst(nums)
    print("")
