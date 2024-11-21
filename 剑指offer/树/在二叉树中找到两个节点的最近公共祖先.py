
'''
https://www.nowcoder.com/practice/e0cc33a83afe4530bcec46eba3325116?
tpId=13&tqId=1024325&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

具体做法：
我们也可以讨论几种情况：
step 1：如果o1和o2中的任一个和root匹配，那么root就是最近公共祖先。
step 2：如果都不匹配，则分别递归左、右子树。
step 3：如果有一个节点出现在左子树，并且另一个节点出现在右子树，则root就是最近公共祖先.
step 4：如果两个节点都出现在左子树，则说明最低公共祖先在左子树中，否则在右子树。
step 5：继续递归左、右子树，直到遇到step1或者step3的情况。
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if root is None:
            return -1
        # 关键终止条件：找到了一个p或者q，任何祖先也是根节点
        if root.val == p or root.val == q:
            return root.val
        leftAncestor = self.lowestCommonAncestor(root.left, p, q)
        rightAncestor = self.lowestCommonAncestor(root.right, p, q)
        if leftAncestor != -1 and rightAncestor != -1:
            return root.val
        elif leftAncestor != -1:
            return leftAncestor
        elif rightAncestor != -1:
            return rightAncestor
        return -1


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().lowestCommonAncestor(pRoot, 4, 5)
    print(results)
