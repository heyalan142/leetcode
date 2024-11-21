class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct_max_binary_tree(nums: [int]) -> TreeNode:
    if len(nums) <= 0:
        return None
    max_value = max(nums)
    max_index = nums.index(max_value)
    node = TreeNode(max_value)
    left_nums = nums[:max_index]
    right_nums = nums[max_index + 1:]
    node.left = construct_max_binary_tree(left_nums)
    node.right = construct_max_binary_tree(right_nums)
    return node


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    tree = construct_max_binary_tree(nums)
    print("f")
