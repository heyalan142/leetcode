class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_binary_tree(in_order: list[int], post_order: list[int]) -> TreeNode:
    if len(post_order) <= 0:
        return None
    root_val = post_order[-1]
    root = TreeNode(root_val)
    separator_idx = in_order.index(root_val)
    left_in_order = in_order[:separator_idx]
    right_in_order = in_order[separator_idx + 1:]
    left_post_order_ = post_order[:len(left_in_order)]
    right_post_order = post_order[len(left_in_order): len(post_order) - 1]
    root.left = build_binary_tree(left_in_order, left_post_order_)
    root.right = build_binary_tree(right_in_order, right_post_order)
    return root


if __name__ == '__main__':
    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]
    tree = build_binary_tree(in_order, post_order)
    print("f")
