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
            '''
            # 注意此处取的是[index:length-1]，而不是[index:length]，因为最后一个值已经取出作为节点值
            '''
            right = self.verifySquenceOfBST(sequence[index:length - 1])
        return left and right


if __name__ == '__main__':
    sequence = [1, 2, 7, 4, 6, 5, 3]
    results = Solution().verifySquenceOfBST(sequence)
    print(results)
