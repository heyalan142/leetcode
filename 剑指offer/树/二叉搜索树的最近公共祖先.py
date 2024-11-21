'''
https://www.nowcoder.com/practice/d9820119321945f588ed6a26f0a6991f?
tpId=13&tqId=2290592&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
我们也可以利用二叉搜索树的性质：对于某一个节点若是p与q都小于等于这个这个节点值，
说明p、q都在这个节点的左子树，而最近的公共祖先也一定在这个节点的左子树；
若是p与q都大于等于这个节点，说明p、q都在这个节点的右子树，而最近的公共祖先
也一定在这个节点的右子树。而若是对于某个节点，p与q的值一个大于等于节点值，一
个小于等于节点值，说明它们分布在该节点的两边，而这个节点就是最近的公共祖先，
因此从上到下的其他祖先都将这个两个节点放到同一子树，只有最近公共祖先会将它们放入
不同的子树，每次进入一个子树又回到刚刚的问题，因此可以使用递归

具体做法：
step 1：首先检查空节点，空树没有公共祖先。
step 2：对于某个节点，比较与p、q的大小，若p、q在该节点两边说明这就是最近公共祖先。
step 3：如果p、q都在该节点的左边，则递归进入左子树。
step 4：如果p、q都在该节点的右边，则递归进入右子树。
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
        if (root.val >= p and root.val <= q) or (root.val <= p and root.val >= q):
            return root.val
        elif root.val >= p and root.val >= q:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    pRoot = TreeNode(2)
    pRoot.left = TreeNode(1)
    pRoot.right = TreeNode(4)
    pRoot.right.left = TreeNode(3)
    pRoot.right.right = TreeNode(5)
    results = Solution().lowestCommonAncestor(pRoot, 3, 5)
    print(results)
