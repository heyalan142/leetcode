'''
https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?
tpId=13&tqId=1374963&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
递归
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror(self, pRoot: TreeNode) -> TreeNode:
        if pRoot is None:
            return None
        leftMirror = self.mirror(pRoot.left)
        rightMirror = self.mirror(pRoot.right)
        pRoot.left = rightMirror
        pRoot.right = leftMirror
        return pRoot


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    mirror = Solution().mirror(pRoot)
    print(mirror)
