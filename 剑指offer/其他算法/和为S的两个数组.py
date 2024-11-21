'''
https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?
tpId=13&tqId=23251&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
思路：
这道题目还有一个条件是数组是升序序列，在方法一中没有用到。这个条件有什么用？既然数组是有序的，那我们肯定
知道和找到一定程度就不找了，我们为什么要从最小的两个数开始相加呢？我们可以用二分法的思路，从中间开始找。
使用双指针指向数组第一个元素和最后一个元素，然后双指针对撞移动，如果两个指针下的和正好等于目标值sum，那我
们肯定找到了，如果和小于sum，说明我们需要找到更大的，那只能增加左边的元素，如果和大于sum，说明我们需要找更
小的，只能减小右边的元素。

具体做法：
step 1：准备左右双指针分别指向数组首尾元素。
step 2：如果两个指针下的和正好等于目标值sum，则找到了所求的两个元素。
step 3：如果两个指针下的和大于目标值sum，右指针左移；如果两个指针下的和小于目标值sum，左指针右移。
step 4：当两指针对撞时，还没有找到，就是数组没有。
'''


class Solution:
    def FindNumbersWithSum(self, array: list[int], sum: int) -> list[int]:
        left = 0
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] == sum:
                return [array[left], array[right]]
            elif array[left] + array[right] > sum:
                right -= 1
            elif array[left] + array[right] < sum:
                left += 1
        return []


if __name__ == '__main__':
    array = [1, 2, 4, 7, 11, 15]
    sum = 15
    val = Solution().FindNumbersWithSum(array, sum)
    print(val)
