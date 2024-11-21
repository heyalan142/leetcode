'''
https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?
tpId=13&tqId=23288&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

step 1：优先判断空数组的特殊情况。
step 2：将数组中的数字元素转换成字符串类型。
step 3：使用冒泡排序，两层遍历数组，每次比较数组相邻位置字符串拼接的大小，如果顺序拼接比逆序拼接更大，则需要交换位置。
step 4：将排序结果再按照字符串拼接成一个整体。
'''


class Solution:
    def PrintMinNumber(self, numbers: list[int]) -> str:
        if not numbers:
            return ""
            # 将数字转成字符
        nums = list(map(str, numbers))
        length = len(nums)
        # 冒泡排序
        for i in range(length - 1, 0,  -1):
            for j in range(0, i):
                s1 = nums[j] + nums[j + 1]
                s2 = nums[j + 1] + nums[j]
                if int(s1) > int(s2):
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return "".join(nums)


if __name__ == '__main__':
    nums = [3, 32, 321]
    val = Solution().PrintMinNumber(nums)
    print(val)
