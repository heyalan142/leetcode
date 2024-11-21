

'''
https://www.nowcoder.com/practice/965fef32cae14a17a8e86c76ffe3131f?
tpId=13&tqId=2277604&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
既然要找所有路径上节点和等于目标值的路径个数，那我们肯定先找这样的路径起点啊，
但是我们不知道起点究竟在哪里，而且任意节点都有可能是起点，那我们就前序遍历二叉树
的所有节点，每个节点都可以作为一次起点，即子树的根节点。
查找路径的时候呢，也需要往下遍历，因此还可以继续前序遍历该子树，在遍历的过程
遇到一个节点，sum相应减少，若是到最后往下的一个节点值正好等于剩下的sum，则找到一种情况。

具体做法：
双重递归，如果必须从跟节点开始则需要单重递归
step 1：每次将原树中遇到的节点作为子树的根节点送入dfs函数中查找有无路径，如果该节点为空则返回。
step 2：然后递归遍历这棵树每个节点，每个节点都需要这样操作。
step 3：在dfs函数中，也是往下递归，遇到一个节点就将sum减去节点值再往下。
step 4：剩余的sum等于当前节点值则找到一种情况。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def findPath(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return self.res
            # 查询以某节点为根的路径数
        self.findTarget(root, sum)
        # 以其子节点为新根
        self.findPath(root.left, sum)
        self.findPath(root.right, sum)
        return self.res

    def findTarget(self, root: TreeNode, sum: int):
        if root is None:
            return
        # 符合目标值
        if sum == root.val:
            self.res += 1
        # 进入子节点继续找
        self.findTarget(root.left, sum - root.val)
        self.findTarget(root.right, sum - root.val)


if __name__ == '__main__':
    pRoot = TreeNode(0)
    pRoot.left = TreeNode(1)
    pRoot.right = TreeNode(1)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().findPath(pRoot, 1)
    print(results)
