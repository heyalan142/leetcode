'''
https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720?
tpId=13&tqId=23448&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''




class Solution:
    def __init__(self):
        self.string = ""
        self.hashMap = dict()

    # 返回对应char
    def FirstAppearingOnce(self):
        for char in self.string:
            if self.hashMap[char] == 1:
                return char
        return "#"

    def Insert(self, char):
        if char in self.hashMap:
            self.hashMap[char] += 1
        else:
            self.hashMap[char] = 1
        self.string = self.string + char
