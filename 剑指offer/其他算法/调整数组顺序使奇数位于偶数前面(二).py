'''
# 具体做法
step1：遍历数组，统计奇数出现的次数，即找到了偶数开始的位置。
step2：准备一个和原数组同样长的新数组承接输出，准备双指针，x指向奇数开始的位置，y指向偶数开始的位置。
step3：遍历原数组，遇到奇数添加在指针x后面，遇到偶数添加在指针y后面，直到遍历结束。
'''


class Solution:
    def reOrderArrayTwo(self, array: list[int]) -> list[int]:
        results = []
        for num in array:
            if num % 2 == 1:
                results.insert(0, num)
            else:
                results.insert(len(array) - 1, num)
        return results


if __name__ == '__main__':
    nums = [1, 4, 4, 3]
    val = Solution().reOrderArrayTwo(nums)
    print(val)
