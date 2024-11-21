'''
https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?
tpId=13&tqId=23289&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
递归函数的参数包含三个信息：遍历序列，树的起点索引位置，树的重点索引位置。
对于后序遍历的二叉搜索树来讲，终点位置就是根，然后从后往前遍历找到的第一个小于终点位置的节点，就是在序列中划分左右子树的分割位置。
只要能够一直划分下去，直到递归最后是单个节点，则说明应该返回true，否则返回false

具体做法：
step 1：首先对于给定列表长度为0的特殊情况返回false
step 2：递归函数中返回条件为 l>=r，返回true
step 3：递归函数中确定根节点为sequence[r]，然后从后往前遍历找到左右子树分割点，进行继续递归
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# 每次取出数组的最后一个树作为节点值，数组分割为前后两个数组，前面数组都是比节点值小，后面数组都是比节点值大。两个数组再递归
'''


class Solution:
    def verifySquenceOfBST(self, sequence: list[int]) -> bool:
        if not sequence:
            return False
        rootValue = sequence[-1]
        length = len(sequence)
        index = 0
        for i in range(length):
            if sequence[i] >= rootValue:
                index = i
                break
        for j in range(index, length):
            if sequence[j] < rootValue:
                return False
        left = True
        if index > 0:
            left = self.verifySquenceOfBST(sequence[0:index])
        right = True
        if index < length - 1:
            # 注意此处取的是[index:length-1]，而不是[index:length]，因为最后一个值已经取出作为节点值
            right = self.verifySquenceOfBST(sequence[index:length - 1])
        return left and right


if __name__ == '__main__':
    sequence = [1, 2, 7, 4, 6, 5, 3]
    results = Solution().verifySquenceOfBST(sequence)
    print(results)
