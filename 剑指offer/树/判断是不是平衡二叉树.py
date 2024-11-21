'''
https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?
tpId=13&tqId=23250&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

递归求高度，不满足条件高度为-1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        return self.getHeight(pRoot) != -1

    def getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        elif abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().IsBalanced_Solution(pRoot)
    print(results)
