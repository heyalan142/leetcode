'''
https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=23288
&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage
%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def PrintMinNumber(self, numbers: list[int]) -> str:
        if not numbers:
            return ""
            # 将数字转成字符
        nums = list(map(str, numbers))
        length = len(nums)
        # 冒泡排序
        for i in range(0, length - 1):
            for j in range(0, length - i - 1):
                s1 = nums[j] + nums[j + 1]
                s2 = nums[j + 1] + nums[j]
                if s1 > s2:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return "".join(nums)


if __name__ == '__main__':
    nums = [3, 32, 321]
    val = Solution().PrintMinNumber(nums)
    print(val)
