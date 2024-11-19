'''
https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b?
tpId=13&tqId=23294&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def treeDepth(self, pRoot: TreeNode) -> int:
        if pRoot is None:
            return 0
        leftDepth = self.treeDepth(pRoot.left)
        rightDepth = self.treeDepth(pRoot.right)
        return max(leftDepth, rightDepth) + 1
