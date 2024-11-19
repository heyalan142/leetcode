'''
https://www.nowcoder.com/practice/57aa0bab91884a10b5136ca2c087f8ff?
tpId=13&tqId=2305268&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking
&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
中序遍历取出数组的第k-1个值
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthNode(self, pRoot: TreeNode, k: int) -> int:
        if k <= 0:
            return -1
        if pRoot is None:
            return -1
        orders = []
        self.middleOrder(pRoot, orders)
        if k > len(orders):
            return -1
        return orders[k-1]

    def middleOrder(self, pRoot: TreeNode, orders: list) -> None:
        if pRoot is None:
            return
        self.middleOrder(pRoot.left, orders)
        orders.append(pRoot.val)
        self.middleOrder(pRoot.right, orders)


if __name__ == '__main__':
    pRoot = TreeNode(1)
    val = Solution().kthNode(pRoot, 0)
    print(val)
