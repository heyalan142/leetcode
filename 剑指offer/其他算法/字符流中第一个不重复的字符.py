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
