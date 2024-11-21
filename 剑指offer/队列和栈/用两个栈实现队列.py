'''
https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?
tpId=13&tqId=23281&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.empty():
            return None
        if self.stack2:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)
