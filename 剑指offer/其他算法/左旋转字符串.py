'''
https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?
tpId=13&tqId=23266&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        length = len(str)
        if length <= 0:
            return ""
        # 取余，因为每次长度为m的旋转数组相当于没有变化
        rol = n % length
        font = str[0:rol]
        end = str[rol:]
        return end + font


if __name__ == '__main__':
    s = ""
    val = Solution().LeftRotateString(s, 6)
    print(val)
