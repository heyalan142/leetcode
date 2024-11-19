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
