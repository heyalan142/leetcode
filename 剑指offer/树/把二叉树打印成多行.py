'''
https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?
tpId=13&tqId=23453&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

具体做法：
step 1：如果树为空，则返回空数组，没有任何打印结果。
step 2：使用队列辅助层次遍历，优先加入二叉树的根节点。
step 3：从根节点开始，每次进入一层的时候，记录队列的长度即本层的节点数，
然后访问相应节点数全在同一个数组中，子节点加入队列中继续排队。
step 4：每次访问完一层将数组加入二维数组中再进入下一层。
'''

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printLines(self, pRoot: TreeNode) -> list[list[int]]:
        results = []
        if pRoot is None:
            return results
        queue = deque()
        queue.append(pRoot)
        while queue:
            result = []
            for i in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(result)
        return results


if __name__ == '__main__':
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    pRoot.left.left = TreeNode(4)
    pRoot.left.right = TreeNode(5)
    results = Solution().printLines(pRoot)
    print(results)
