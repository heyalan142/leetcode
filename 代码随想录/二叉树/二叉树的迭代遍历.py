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
        result.append(node.value)
        # 右孩子先入栈
        if node.right:
            stack.append(node.right)
        # 左孩子后入栈
        if node.left:
            stack.append(node.left)
    return result


# 左中右
def inorder_traversal(tree: TreeNode) -> list[int]:
    result = []
    if tree is None:
        return result
    current = tree
    stack = []
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.value)
            # 取栈顶元素右结点
            cur = cur.right
    return result


# 左右中
def postorder_traversal(tree: TreeNode) -> list[int]:
    result = []
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
    result = preorder_traversal(tree)
    print(result)
