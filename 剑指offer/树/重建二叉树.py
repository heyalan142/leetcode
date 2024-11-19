'''
https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&
tqId=23282&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl
=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
前序遍历，我们知道序列的第一个元素必定是根节点的值。然后在中序遍历中找出根节点位置，根节点左右
区域为左子树中序遍历数组，右子树中序遍历数组。再把前序遍历找出左子树前序遍历数组和右子树前序遍历数组。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, preOrder: list[int], vinOrder: list[int]) -> TreeNode:
        if len(preOrder) <= 0 or len(vinOrder) <= 0:
            return None
        root = preOrder[0]
        tree = TreeNode(root)
        rootIndex = vinOrder.index(root)
        leftVinOrder = vinOrder[0:rootIndex]
        rightVinOrder = vinOrder[rootIndex + 1:]
        leftPreOrder = preOrder[1: len(leftVinOrder) + 1]
        rightPreOrder = preOrder[len(leftVinOrder) + 1:]
        tree.left = self.reConstructBinaryTree(leftPreOrder, leftVinOrder)
        tree.right = self.reConstructBinaryTree(rightPreOrder, rightVinOrder)
        return tree


if __name__ == '__main__':
    preOrder = [1, 2, 4, 7, 3, 5, 6, 8]
    vinOrder = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = Solution().reConstructBinaryTree(preOrder, vinOrder)
    print(tree)
