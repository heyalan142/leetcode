class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中左右
def preorderTraversal(root: TreeNode) -> list[int]:
    res = []

    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


# 左中右
def inorderTraversal( root: TreeNode) -> list[int]:
    res = []

    def dfs(node):
        if node is None:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


# 左右中
def postorderTraversal(root: TreeNode) -> list[int]:
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res


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
    result = preorderTraversal(tree)
    print(result)
