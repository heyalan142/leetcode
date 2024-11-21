'''
https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?
tpId=13&tqId=23258&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        result = s.replace(" ", "%20")
        return result
