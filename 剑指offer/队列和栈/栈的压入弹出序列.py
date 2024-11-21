'''
https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?
tpId=13&tqId=23290&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
如果出栈数组里的元素在辅助栈里但是却不是栈顶元素，则不符合栈的压入和弹出序列

具体做法：
step 1：准备一个辅助栈，两个下标分别访问两个序列。
step 2：辅助栈为空或者栈顶不等于出栈数组当前元素，就持续将入栈数组加入栈中。
step 3：栈顶等于出栈数组当前元素就出栈。
step 4：当入栈数组访问完，出栈数组无法依次弹出，就是不匹配的，否则两个序列都访问完就是匹配的。
'''



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
