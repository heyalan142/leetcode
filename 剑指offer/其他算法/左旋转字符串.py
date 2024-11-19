
class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        length = len(str)
        if length <= 0:
            return ""
        rol = n % length
        font = str[0:rol]
        end = str[rol:]
        return end + font





if __name__ == '__main__':
    s = ""
    val = Solution().LeftRotateString(s, 6)
    print(val)
