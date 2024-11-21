'''
https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?
tpId=13&tqId=23287&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''

import str as str

class Solution:
    def ReverseSentence(self, str: str) -> str:
        words = str.split(" ")
        while "" in words:
            words.remove("")
        left = 0
        right = len(words) - 1
        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -= 1
        return " ".join(words)


if __name__ == '__main__':
    str = "nowcoder. a am I"
    reverseStr = Solution().ReverseSentence(str)
    print(reverseStr)
