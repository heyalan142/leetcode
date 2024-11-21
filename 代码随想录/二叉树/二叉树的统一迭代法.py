class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 中左右
def preorder_traversal(root: TreeNode) -> list[int]:
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            node = stack.pop()
            result.append(node.value)
        else:
            if node.right:  # 右
                stack.append(node.right)
            if node.left:  # 左
                stack.append(node.left)
            stack.append(node)
            stack.append(None)
    return result


# 左中右
def inorder_traversal(root: TreeNode) -> list[int]:
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            node = stack.pop()
            result.append(node.value)
        else:
            if node.right:  # 右
                stack.append(node.right)
            stack.append(node)
            stack.append(None)
            if node.left:  # 左
                stack.append(node.left)

    return result


# 左右中
def postorder_traversal(root: TreeNode) -> list[int]:
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            node = stack.pop()
            result.append(node.value)
        else:
            stack.append(node)
            stack.append(None)
            if node.right:  # 右
                stack.append(node.right)
            if node.left:  # 左
                stack.append(node.left)
    return result


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
    # result = preorder_traversal(tree)
    # result = inorder_traversal(tree)
    result = postorder_traversal(tree)
    print(result)
