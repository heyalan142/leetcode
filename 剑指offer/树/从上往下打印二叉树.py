
'''
https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?
tpId=13&tqId=23280&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

具体做法：
step 1：首先判断二叉树是否为空，空树没有遍历结果。
step 2：建立辅助队列，根节点首先进入队列。不管层次怎么访问，根节点一定是第一个，那它肯定排在队伍的最前面。
step 3：每次遍历队首节点，如果它们有子节点，依次加入队列排队等待访问。
'''


from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# 使用队列，每次取出队列里的第一个树节点，然后把树节点的左右树节点加进去
'''
class Solution:
    def printFromTopToBottom(self, root: TreeNode) -> list[int]:
        results = []
        if root is None:
            return results
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            results.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().printFromTopToBottom(pRoot)
    print(results)
