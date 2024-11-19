class Solution:
    def IsPopOrder(self, pushV: list[int], popV: list[int]) -> bool:
        tempStack = []
        popLength = len(popV)
        j = 0
        for i in range(popLength):
            while j < len(pushV) and (len(tempStack) == 0 or tempStack[-1] != popV[i]):
                tempStack.append(pushV[j])
                j += 1
            if tempStack[-1] == popV[i]:
                tempStack.pop()
            else:
                return False
        return True


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 3, 5, 1, 2]
    isPopOrder = Solution().IsPopOrder(pushV, popV)
    print(isPopOrder)
