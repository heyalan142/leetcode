
'''
https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?
tpId=13&tqId=23293&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot1 is None and pRoot2 is not None:
            return False
        if pRoot1 is None and pRoot2 is None:
            return True
        '''
        # 关键终止条件：父树不为空但是子树为空，代表是相同的树
        '''
        if pRoot1 is not None and pRoot2 is None:
            return True
        '''
        # 关键终止条件
        '''
        return pRoot1.val == pRoot2.val and self.isSameTree(pRoot1.left, pRoot2.left) and self.isSameTree(pRoot1.right,
                                                                                                          pRoot2.right)

    def hasSubtree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot2 is None:
            return False
        if pRoot1 is None and pRoot2 is not None:
            return False
        if pRoot1 is None and pRoot2 is  None:
            return True
        isSameTree = self.isSameTree(pRoot1, pRoot2)
        leftHasSubtree = self.hasSubtree(pRoot1.left, pRoot2)
        rightHasSubtree = self.hasSubtree(pRoot1.right, pRoot2)
        return leftHasSubtree or rightHasSubtree or isSameTree


if __name__ == '__main__':
    pRoot1 = TreeNode(1)
    pRoot1.left = TreeNode(2)
    pRoot1.right = TreeNode(3)
    pRoot1.left.left = TreeNode(4)
    pRoot1.left.right = TreeNode(5)
    pRoot2 = TreeNode(3)
    # pRoot2.left = TreeNode(2)
    # pRoot2.right = TreeNode(3)

    hasSubtree = Solution().hasSubtree(pRoot1, pRoot2)
    print(hasSubtree)
