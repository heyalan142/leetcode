'''
https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?
tpId=13&tqId=23268&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
在push的时候就将最小值记录下来，由于栈先进后出的特殊性，我们可以构造一个单调栈，保证栈内元
素都是递增的，栈顶元素就是当前最小的元素。

具体做法：
step 1：使用一个栈记录进入栈的元素，正常进行push、pop、top操作。
step 2：使用另一个栈记录每次push进入的最小值。
step 3：每次push元素的时候与第二个栈的栈顶元素比较，若是较小，则进入
第二个栈，若是较大，则第二个栈的栈顶元素再次入栈，因为即便加了一个元素，
它依然是最小值。于是，每次访问最小值即访问第二个栈的栈顶。
'''


class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, node):
        self.s1.append(node)
        if len(self.s2) == 0 or self.s2[-1] > node:
            self.s2.append(node)
        else:
            # 重复加入栈顶
            self.s2.append(self.s2[-1])

    def pop(self):
        self.s1.pop()
        self.s2.pop()

    def top(self):
        return self.s1[-1]

    def min(self):
        return self.s2[-1]

if __name__ == '__main__':
    sulution = Solution()
    sulution.push(-1)
    sulution.push(-2)
    sulution.push(1)
    minValue = sulution.min()
    print(minValue)
