'''
https://www.nowcoder.com/practice/ef1f53ef31ca408cada5093c8780f44b?
tpId=13&tqId=1374930&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
# 具体做法
step1：遍历数组，统计奇数出现的次数，即找到了偶数开始的位置。
step2：准备一个和原数组同样长的新数组承接输出，准备双指针，x指向奇数开始的位置，y指向偶数开始的位置。
step3：遍历原数组，遇到奇数添加在指针x后面，遇到偶数添加在指针y后面，直到遍历结束。
'''


class Solution:
    def reOrderArray(self, array: list[int]) -> list[int]:
        count = 0
        for num in array:
            if num % 2 == 1:
                count += 1
        left = 0
        right = count
        results = [0 for _ in range(len(array))]
        for num in array:
            if num % 2 == 1:
                results[left] = num
                left += 1
            else:
                results[right] = num
                right += 1
        return results


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    val = Solution().reOrderArray(nums)
    print(val)
